name: YouTube Automation
on:
  schedule:
    - cron: '0 0 * * *' # هادي كتعني يخدم كل نهار مع منتصف الليل
  workflow_dispatch: # هاد الزر كيخليك تخدم السكريبت يدوياً وقتما بغيتي

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      
      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install yt-dlp
      
      - name: Run script
        run: python main.py
