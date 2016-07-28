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