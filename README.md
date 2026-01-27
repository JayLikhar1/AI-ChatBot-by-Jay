# AI-Powered Chatbot by Jay Likhar

A Chatbot application made by using Groq's fast AI models.

## Features

- 🤖 Powered by Groq's Llama 3.1 8B Instant model
- 🎨 Minimal Apple/iOS design with system fonts
- 💬 Real-time chat interface
- ⚡ Fast responses with Groq's inference engine
- 🌙 Beautiful dark mode UI

## Local Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd AI-ChatBot-App
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Copy `.env.example` to `.env`
   - Add your Groq API key:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```
   - Get a free API key at [console.groq.com](https://console.groq.com)

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

## Deploy to Streamlit Cloud

### Step 1: Push to GitHub

1. **Initialize git repository** (if not already done)
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Create a new repository on GitHub**
   - Go to [github.com](https://github.com) and create a new repository
   - Don't initialize with README (you already have one)

3. **Push your code**
   ```bash
   git remote add origin https://github.com/yourusername/your-repo-name.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy on Streamlit Cloud

1. **Go to Streamlit Cloud**
   - Visit [streamlit.io/cloud](https://streamlit.io/cloud)
   - Sign in with your GitHub account

2. **Deploy your app**
   - Click "New app"
   - Select your repository
   - Choose the branch (usually `main`)
   - Set the main file path to `app.py`

3. **Add your API key**
   - In the app settings, go to "Secrets"
   - Add your Groq API key:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```
   - Click "Save"

4. **Launch your app**
   - Your app will be available at `https://your-app-name.streamlit.app`
   - Streamlit Cloud will automatically redeploy on every push to your main branch

## Environment Variables

The app requires the following environment variable:

- `GROQ_API_KEY`: Your Groq API key (get it free at [console.groq.com](https://console.groq.com))

## Tech Stack

- **Streamlit**: Web framework
- **LangChain**: LLM integration
- **Groq**: Fast AI inference
- **Python-dotenv**: Environment variable management

## License

Free to use and modify.

## Author

Jay Likhar
