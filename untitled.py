from datasets import load_dataset

# Frequency data
freq = load_dataset(
    "mabilton/fremtpl2",
    "freMTPL2freq",
    split="train"
).to_pandas()

# Severity data
sev = load_dataset(
    "mabilton/fremtpl2",
    "freMTPL2sev",
    split="train"
).to_pandas()

print(freq.shape)
print(sev.shape)

print(freq.head())
print(sev.head())