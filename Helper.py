import math
from DataService import DataService
import operator
from pymongo import MongoClient
class Helper(object):
	@classmethod
	def cosine_similarity(cls, app_list1, app_list2):
		match_count = cls.__count_match(app_list1, app_list2)
		return float(match_count) / math.sqrt(len(app_list1) * len(app_list2))
	@classmethod
	def __count_match(cls, list1, list2):
		count = 0
		for element in list1:
			if element in list2:
				count += 1
		return count

def calculate_top_5(app, user_download_history):
	app_similarity = {}

	for apps in user_download_history:
		similarity = Helper.cosine_similarity([app], apps)
		for other_app in apps:
			if app_similarity.has_key(other_app):
				app_similarity[other_app] = app_similarity[other_app] + similarity
			else:
				app_similarity[other_app] = similarity
	if not app_similarity.has_key(app):
		return

	app_similarity.pop(app)
	sorted_tups = sorted(app_similarity.items(), key = operator.itemgetter(1), reverse=True)
	top_5_app = [sorted_tups[0][0], sorted_tups[1][0], sorted_tups[2][0], sorted_tups[3][0], sorted_tups[4][0]]
	print("top_5_app for" + str(app) + ":\t" + str(top_5_app))


def main():
	try:
		client = MongoClient('localhost', 27017)
		DataService.init(client)

		user_download_history = DataService.retrieve_user_download_history()
		calculate_top_5('C10107104', user_download_history.values())
	except Exception as e:
		print (e)
	finally:
		if 'client' in locals():
			client.close()

if __name__ == "__main__":
	main()