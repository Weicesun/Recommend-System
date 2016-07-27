from pymongo import MongoClient
import random

class DataService(object):
	@classmethod
	def init(cls, client):
		cls.client = client
		cls.db = client.appstore
		cls.user_download_history = cls.db.user_download_history
		cls.app_info = cls.db.app_info
	@classmethod
	def retrieve_user_download_history(cls, filter_dict={}):
		result = {}
		cursor = cls.user_download_history.find(filter_dict)
		for user_download_history in cursor:
			result[user_download_history['user_id']] = user_download_history['download_history']

		return result