```python
# config.py

# Database configuration
DATABASE_CONFIG = {
    'host': 'localhost',
    'dbname': 'ai_adaptive_tutor',
    'user': 'root',
    'password': 'password',
    'port': 5432
}

# Server configuration
SERVER_CONFIG = {
    'host': 'localhost',
    'port': 5000
}

# Machine Learning model path
ML_MODEL_PATH = 'models/ml_model.pkl'

# Natural Language Processing model path
NLP_MODEL_PATH = 'models/nlp_model.pkl'

# Secret key for session management
SECRET_KEY = 'your-secret-key'

# Directory for storing user interface files
UI_DIR = 'static/'

# Directory for storing content creation toolkit files
TOOLKIT_DIR = 'toolkit/'

# Test configuration
TEST_CONFIG = {
    'test_db': 'test_db',
    'test_user': 'test_user',
    'test_password': 'test_password'
}
```
