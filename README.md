# eCourt-Automation-API-n8n-Workflow-Integration


📄 eCourt Automation with n8n – README

This workflow automates the scraping of Indian eCourt data based on a CNR number.

✅ Requirements:
- Your scraper API (`scraper_api.py`) must be running locally at http://localhost:5000/scrape
- CNR input must be submitted via n8n webhook

🔧 How to Use:
1. Import `ecourt_n8n_workflow.json` into your n8n instance.
2. Copy the Webhook URL from the Webhook node.
3. Submit a POST request to that webhook with this body:
   {
     "cnr": "HRFB010018772023"
   }
4. The HTTP Request node sends the CNR to your local API.
5. The API returns JSON case data (party name, FIR, etc.).
6. The Set node extracts and formats these values.

📤 You can connect the Set node to:
- Google Sheets (to log results)
- Gmail/SendGrid (to send case info via email)

✅ All dynamic expressions are configured already.
