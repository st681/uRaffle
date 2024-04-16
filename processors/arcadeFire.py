from entryProcessor import EntryProcessor

class arcadeFire(EntryProcessor):
    def requiredFields(self):
        return ["email", "proxy"]
    def process(self, entry):
        print(entry)
        print(f"Processing Raffle Type A entry for {entry['email']}")
