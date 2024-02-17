import requests

def fetch_latest_projects():
    # Make requests to the GitHub API to fetch the latest projects from multiple repositories
    # Parse the responses to extract project information
    # Return a list of project details (name, description, URL, icon/image URL)

    # Define a list of repositories
    repositories = [
        {'username': 'SubFabula', 'repository_name': 'QR-Plus'},
        # Add more repositories as needed
    ]
    
    projects = []
    
    # Iterate over each repository
    for repo in repositories:
        # Construct the API URL for the repository
        api_url = f"https://api.github.com/repos/{repo['username']}/{repo['repository_name']}/projects"
        
        # Make a GET request to the API endpoint
        response = requests.get(api_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            projects_data = response.json()
            
            # Extract project information from the response
            for project in projects_data:
                project_name = project['name']
                project_description = project['description']
                project_url = project['html_url']
                # Extract other project details as needed
                
                # Append project details to the list
                projects.append({
                    'name': project_name,
                    'description': project_description,
                    'url': project_url
                    # Add other project details as needed
                })
        else:
            # Handle unsuccessful API request
            print(f"Failed to fetch projects from GitHub API for repository: {repo['repository_name']}")
    
    return projects

def generate_markdown(projects):
    # Generate Markdown content for each project
    markdown_content = ""
    for project in projects:
        markdown_content += f"- [{project['name']}]({project['url']}) - {project['description']}\n"
    return markdown_content

def update_readme(content):
    # Read the README.md file
    with open('README.md', 'r') as file:
        readme_content = file.read()
    # Find the placeholder <!-- Placeholder for dynamically generated content -->
    # Replace the placeholder with the generated Markdown content
    updated_readme = readme_content.replace("<!-- Placeholder for dynamically generated content -->", content)
    # Write the updated content back to the README.md file
    with open('README.md', 'w') as file:
        file.write(updated_readme)

def main():
    projects = fetch_latest_projects()
    markdown_content = generate_markdown(projects)
    update_readme(markdown_content)

if __name__ == "__main__":
    main()
