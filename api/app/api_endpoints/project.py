from app import flask_app











# import requests
# import shutil

# def generate_spring_boot_project(project_type, language,  group_id, artifact_id, dependencies, java_version='11', packaging='jar'):
#     # Define the URL for Spring Initializr API
#     url = 'https://start.spring.io/starter.zip'

#     # Define payload for POST request
#     payload = {
#         'type': project_type,
#         'language': language,
#         'groupId': group_id,
#         'artifactId': artifact_id,
#         'javaVersion': java_version,
#         'packaging': packaging,
#         'dependencies': dependencies
#     }

#     # Send POST request to generate the project
#     response = requests.post(url, data=payload, stream=True)

#     # Check if request was successful
#     if response.status_code == 200:
#         # Save the generated ZIP file
#         with open(f'{artifact_id}.zip', 'wb') as zip_file:
#             response.raw.decode_content = True
#             shutil.copyfileobj(response.raw, zip_file)
#         print(f'Successfully generated project: {artifact_id}.zip')
#     else:
#         print('Failed to generate project.')
