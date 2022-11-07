global model_path
model_path = "engwords.nlpdm"
class NLP():
    def words(*args):
        words = open(model_path,"r+")
        return words.read()
        
    def getwords(key="a",count=None):
        words = []
        for line in open(model_path):
            words += [w for w in line.split() if w.startswith(str(key))]
            if count == None:
                read = words
                return read
            else:
                read = words[:int(count)]
                return read
class load(NLP):
    def lang_model(path):
        import os.path
        if os.path.isfile(path) == True:
            model_path = path
        else:
            raise FileNotFoundError(f'File "{path}" is not exists')



