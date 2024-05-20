import looker_sdk

sdk = looker_sdk.init40()
my_user = sdk.me()

print(my_user["first_name"])

for folder in sdk.all_folders():
    print(f"{folder['created_at']} - {folder['name']}")
    print(folder.keys)
