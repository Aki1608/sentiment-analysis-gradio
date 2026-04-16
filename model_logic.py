class ModelLogic:
    from transformers import pipeline

    try:
        classifier = pipeline('sentiment-analysis', 'Xenova/distilbert-base-uncased-finetuned-sst-2-english')
    except Exception as e:
        print(f"Failed to initialize pipeline: {e}")

    def get_prediction(text):
        output = classifier(text)
        
        label = output['label']
        confidence = output['score']

        print(f"The text sentiment is: {label} with the confidence score: {score}.")