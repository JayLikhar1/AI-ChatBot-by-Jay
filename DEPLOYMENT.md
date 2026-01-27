# Deployment Guide for Streamlit Cloud

## Quick Deployment Steps

### ✅ Pre-Deployment Checklist

- [x] All code is in `app.py`
- [x] `requirements.txt` is up to date
- [x] `.gitignore` excludes `.env` file
- [x] No hardcoded API keys in code
- [x] Environment variables are loaded via `os.getenv()`

### 🚀 Deployment Steps

#### 1. Prepare Your Code

Your code is already ready! The app uses:
- `load_dotenv()` for local development
- `os.getenv()` which works on Streamlit Cloud automatically

#### 2. Push to GitHub

```bash
# Initialize git (if not done)
git init

# Add all files
git add .

# Commit
git commit -m "Ready for deployment"

# Add remote (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git push -u origin main
```

#### 3. Deploy on Streamlit Cloud

1. **Go to**: [share.streamlit.io](https://share.streamlit.io)
2. **Sign in** with your GitHub account
3. **Click**: "New app"
4. **Fill in**:
   - Repository: Select your GitHub repo
   - Branch: `main`
   - Main file path: `app.py`
5. **Click**: "Deploy!"

#### 4. Add Your API Key

1. In your app's dashboard, click **"⚙️ Settings"**
2. Go to **"Secrets"** tab
3. Add your Groq API key:
   ```
   GROQ_API_KEY=your_actual_api_key_here
   ```
4. Click **"Save"**
5. Your app will automatically redeploy

### 🔗 Your App URL

After deployment, your app will be available at:
```
https://YOUR-APP-NAME.streamlit.app
```

### 📝 Notes

- **Automatic Updates**: Every time you push to your main branch, Streamlit Cloud will automatically redeploy your app
- **Secrets**: Never commit your `.env` file. Use Streamlit Cloud's Secrets feature instead
- **Free Tier**: Streamlit Cloud offers free hosting with some limitations
- **API Keys**: Keep your Groq API key secure and don't share it publicly

### 🐛 Troubleshooting

**App won't start?**
- Check that `requirements.txt` has all dependencies
- Verify your API key is set correctly in Secrets
- Check the logs in Streamlit Cloud dashboard

**API errors?**
- Verify your Groq API key is valid
- Check your Groq account quota at [console.groq.com](https://console.groq.com)

**Styling issues?**
- Clear browser cache
- Check that CSS is loading correctly

### ✨ You're All Set!

Your app should now be live and accessible to anyone with the link!
