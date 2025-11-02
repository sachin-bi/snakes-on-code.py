
class ChaiCode:
    @staticmethod       #   --> this is decorator
    def filterInArray(text):
        return [item.strip() for item in text.split(",")]
    

raw = "  water, ginger , salt " 
print(ChaiCode.filterInArray(raw))