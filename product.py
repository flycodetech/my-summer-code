import os

def find_job_applications(folder_path):
    job_letters = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if "job" in file.lower() or "application" in file.lower() or "cover letter" in file.lower():
                job_letters.append(os.path.join(root, file))
    return job_letters

if __name__ == "__main__":
    # Change this to your Linked folder path
    linked_folder = "/path/to/your/Linked"
    job_letters = find_job_applications(linked_folder)
    print("Job application letters found:")
    for letter in job_letters:
        print(letter)