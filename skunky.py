import json

nfts = []

# Generate 7100 NFT objects
for i in range(1, 7101):
    nft = {
        "id": i,
        "name": "ZGenetics Strain",
        "description": f"ZGenetics Strain THC% Terpene Profile",
        "image": f"./skunkberryOG.mp4"
    }
    nfts.append(nft)

# Create a dictionary to hold the NFT array
data = {
    "nfts": nfts
}

# Convert the dictionary to JSON and save to a file
with open("nfts.json", "w") as f:
    json.dump(data, f)
