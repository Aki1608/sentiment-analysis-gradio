from transformers import pipeline

class ModelLogic:
    try:
        classifier = pipeline('sentiment-analysis', 'distilbert-base-uncased-finetuned-sst-2-english')
    except Exception as e:
        print(f"Failed to initialize pipeline: {e}")
        classifier = None

    @staticmethod
    def get_prediction(text):
        if ModelLogic.classifier is None:
            return "Model not loaded."

        output = ModelLogic.classifier(text)
        res = output[0]
        
        label = res['label']
        confidence = res['score']

        return f"The text sentiment is: {label} with the confidence score: {confidence:.2f}."