import kagglehub

path = kagglehub.dataset_download(
    "naserabdullahalam/phishing-email-dataset"
)

print("Dataset downloaded to:", path)
