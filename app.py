def get_data():
    data = [
        {"input": "Can Lamini handle nested JSON structures?", 
         "output": "Yes, Lamini's type system supports complex nested JSON structures through Pydantic's BaseModel."},

        {"input": "How does Lamini ensure data validation?", 
         "output": "Lamini uses Pydantic's built-in validation features to ensure data integrity and correctness."},

        {"input": "Is it possible to use custom validators in Lamini?", 
         "output": "Yes, Lamini allows the use of custom validators within Pydantic models for specialized data validation needs."},

        {"input": "Does Lamini integrate with FastAPI for API development?", 
         "output": "Yes, Lamini seamlessly integrates with FastAPI, leveraging Pydantic models for request and response data handling."},

        {"input": "Can Lamini models be extended with additional fields?", 
         "output": "Yes, Lamini models can be easily extended with additional fields using Pydantic's inheritance and model composition."},

        {"input": "How does Lamini handle optional fields?", 
         "output": "Lamini uses Pydantic's `Optional` type annotation to define fields that may or may not be present in the data."}
    ]
    return data
import lamini
from lamini import Lamini
lamini.api_key='99dccbe32f31a569d564b65a4136038dd634842d5e2b58f6c923699bd84dcc38'

llm=Lamini(model_name="meta-llama/Meta-Llama-3-8B-Instruct")
data=get_data()
llm.tune(data_or_dataset_id=data,
         finetune_args={'learning_rate':1.0e-4})
"""
common hyperparamerters to tune include"
learning rate(float)-the learning rate of the model
early stopping(bool)
max_steps(int)
optim(str)"""
