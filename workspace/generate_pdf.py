import os
from fpdf import FPDF

class DocumentationPDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_text_color(100, 100, 100)
            self.set_font('Helvetica', 'I', 8)
            self.cell(0, 10, 'OpenClaw WhatsApp AI Bot (Nova) - Project Documentation', border=0, align='L')
            self.cell(0, 10, f'Page {self.page_no()}', border=0, align='R')
            self.ln(12)
            # Draw a thin header line
            self.set_draw_color(220, 220, 220)
            self.set_line_width(0.2)
            self.line(15, 20, 195, 20)

    def footer(self):
        if self.page_no() > 1:
            self.set_y(-15)
            self.set_text_color(150, 150, 150)
            self.set_font('Helvetica', 'I', 8)
            self.cell(0, 10, 'CONFIDENTIAL & PRIVATE - FOR SYSTEM OWNER USE ONLY', border=0, align='C')

    def add_title_page(self):
        self.add_page()
        # Add background decorative sidebar
        self.set_fill_color(30, 41, 59) # Dark Slate Blue
        self.rect(0, 0, 15, 297, 'F')
        
        self.set_left_margin(30)
        self.set_y(60)
        
        # Super title
        self.set_text_color(100, 116, 139)
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 10, 'SYSTEM ARCHITECTURE & OPERATIONAL GUIDE', ln=True)
        
        # Main Title
        self.set_text_color(15, 23, 42) # Near Black
        self.set_font('Helvetica', 'B', 28)
        self.multi_cell(0, 15, 'OpenClaw WhatsApp\nAI Bot (Nova)')
        self.ln(10)
        
        # Decorative divider line
        self.set_draw_color(99, 102, 241) # Indigo Blue
        self.set_line_width(1.5)
        self.line(30, self.get_y(), 100, self.get_y())
        self.ln(15)
        
        # Description
        self.set_text_color(71, 85, 105)
        self.set_font('Helvetica', '', 12)
        description_text = (
            "A comprehensive technical manual documenting the design, implementation, "
            "configuration, and operation of the locally hosted OpenClaw WhatsApp agent. "
            "Includes details on the integration with Ollama (Llama 3.2 1B), character "
            "guidelines (Nova), security token configuration, and troubleshooting."
        )
        self.multi_cell(0, 7, description_text)
        
        # Meta info at the bottom
        self.set_y(220)
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(15, 23, 42)
        self.cell(0, 6, 'Created For:', ln=True)
        self.set_font('Helvetica', '', 10)
        self.set_text_color(71, 85, 105)
        self.cell(0, 6, 'System Administrator ([YOUR_PHONE_NUMBER])', ln=True)
        self.ln(4)
        
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(15, 23, 42)
        self.cell(0, 6, 'Date:', ln=True)
        self.set_font('Helvetica', '', 10)
        self.set_text_color(71, 85, 105)
        self.cell(0, 6, 'May 20, 2026', ln=True)
        self.ln(4)
        
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(15, 23, 42)
        self.cell(0, 6, 'Deployment Type:', ln=True)
        self.set_font('Helvetica', '', 10)
        self.set_text_color(71, 85, 105)
        self.cell(0, 6, 'Localhost Loopback (Windows Service Scheduler)', ln=True)
        
        # Reset margins for the rest of the pages
        self.set_left_margin(15)
        self.set_right_margin(15)

    def heading_1(self, text):
        self.ln(8)
        self.set_text_color(30, 41, 59)
        self.set_font('Helvetica', 'B', 16)
        self.cell(0, 10, text, ln=True)
        # Thin bar below header
        self.set_draw_color(99, 102, 241)
        self.set_line_width(0.5)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(5)

    def heading_2(self, text):
        self.ln(4)
        self.set_text_color(71, 85, 105)
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 8, text, ln=True)
        self.ln(2)

    def paragraph(self, text):
        self.set_text_color(51, 65, 85)
        self.set_font('Helvetica', '', 10)
        self.multi_cell(0, 6, text)
        self.ln(3)

    def bullet_point(self, bold_text, normal_text):
        self.set_text_color(51, 65, 85)
        self.set_font('Helvetica', '', 10)
        self.write(6, ' - ')
        self.set_font('Helvetica', 'B', 10)
        self.write(6, bold_text + ': ')
        self.set_font('Helvetica', '', 10)
        self.write(6, normal_text + '\n')
        self.ln(1.5)

    def code_block(self, text):
        self.ln(2)
        self.set_fill_color(248, 250, 252) # Slate-50 background
        self.set_text_color(15, 23, 42)
        self.set_font('Courier', '', 9)
        
        # Add padding by drawing cell background
        lines = text.strip().split('\n')
        for line in lines:
            # Weasy cell width
            self.cell(0, 5, '  ' + line, ln=True, fill=True)
        self.ln(3)

# Initialize PDF
pdf = DocumentationPDF()
pdf.set_auto_page_break(auto=True, margin=20)
pdf.add_title_page()

# ----------------- PAGE 2: INTRODUCTION & ARCHITECTURE -----------------
pdf.add_page()
pdf.heading_1("1. Project Introduction & Overview")
pdf.paragraph(
    "The OpenClaw WhatsApp AI Assistant project (Nova) is a self-hosted, private intelligence system "
    "operating entirely on the host machine. By marrying WhatsApp Web protocols with local Large "
    "Language Models (LLMs), it creates a secure, agentic personal companion. Unlike cloud-based chatbots, "
    "all data, conversation logs, and document retrieval remain stored on your local disk, ensuring absolute privacy."
)

pdf.heading_2("Project Objectives")
pdf.bullet_point("Data Privacy", "All message logs and files stay on your machine, away from commercial server databases.")
pdf.bullet_point("Zero Latency & Cost", "Runs on local GPUs/CPUs using Ollama, which requires no subscription fee or API cost.")
pdf.bullet_point("Custom Personality", "Fully customizable behavior guidelines through markdown templates (SOUL.md).")
pdf.bullet_point("Security", "Allowlist controls restrict access solely to authorized numbers, preventing public spam.")

pdf.heading_1("2. Component Architecture")
pdf.paragraph(
    "The workspace acts as an ecosystem composed of four primary layers that operate in constant synchronization:"
)

# Text-based architecture diagram
pdf.code_block(
    "+-----------------------------+\n"
    "|   Your Phone (WhatsApp)     |\n"
    "+--------------+--------------+\n"
    "               | (Direct Message via WhatsApp Web Channel)\n"
    "               v\n"
    "+-----------------------------+\n"
    "|   OpenClaw Gateway Service  | <--- Port 18789 (Authorized connection)\n"
    "+--------------+--------------+\n"
    "               |                              ^\n"
    "               | (Loads guidelines)           | (Generates response)\n"
    "               v                              |\n"
    "+-----------------------------+       +-------+---------------------+\n"
    "|      Workspace Config       |       |       Ollama LLM Engine     |\n"
    "| (SOUL.md, USER.md, etc.)    |       |  (Llama 3.2 1B Active)      |\n"
    "+-----------------------------+       +-----------------------------+"
)

pdf.paragraph(
    "1. WhatsApp Interface: The user initiates communication by sending a message from their phone to the bot.\n"
    "2. OpenClaw Gateway: The gateway processes WebSocket requests and manages the session context. It checks the configuration to ensure the sender is allowed.\n"
    "3. Workspace Config: The system reads identity files and memory files to assemble the instruction context.\n"
    "4. Ollama LLM Engine: Generates the reply dynamically based on the model specified (e.g. Llama 3.2 1B)."
)

# ----------------- PAGE 3: KEY CONFIGURATION FILES -----------------
pdf.add_page()
pdf.heading_1("3. Core Configuration Files")
pdf.paragraph(
    "The operational aspects, security tokens, allowed contacts, and default models are specified in the "
    "root configurations. Below are details of the active settings files."
)

pdf.heading_2("openclaw.json - Gateway & Channel Settings")
pdf.paragraph(
    "This file resides in the root directory and configures how the daemon connects to local LLMs and channels:"
)
pdf.code_block(
    "{\n"
    "  \"models\": {\n"
    "    \"providers\": {\n"
    "      \"ollama\": {\n"
    "        \"baseUrl\": \"http://127.0.0.1:11434\",\n"
    "        \"models\": [ { \"id\": \"llama3.2:1b\", \"name\": \"Llama 3.2 1B\" } ]\n"
    "      }\n"
    "    }\n"
    "  },\n"
    "  \"agents\": {\n"
    "    \"defaults\": {\n"
    "      \"model\": { \"primary\": \"ollama/llama3.2:1b\" }\n"
    "    }\n"
    "  },\n"
    "  \"gateway\": {\n"
    "    \"mode\": \"local\",\n"
    "    \"auth\": {\n"
    "      \"mode\": \"token\",\n"
    "      \"token\": \"eca89116dc38143ce692d733d290850697fe90f11af3a86c\"\n"
    "    }\n"
    "  },\n"
    "  \"channels\": {\n"
    "    \"whatsapp\": {\n"
    "      \"enabled\": true,\n"
    "      \"selfChatMode\": true,\n"
    "      \"dmPolicy\": \"allowlist\",\n"
    "      \"allowFrom\": [ \"[YOUR_PHONE_NUMBER]\" ]\n"
    "    }\n"
    "  }\n"
    "}"
)
pdf.paragraph(
    "Key configuration definitions:\n"
    " - ollama.baseUrl: Points to the local Ollama daemon port (11434).\n"
    " - gateway.auth: Configures token security to prevent unauthorized Control UI connections.\n"
    " - channels.whatsapp.allowFrom: A whitelist array containing phone numbers authorized to chat with Nova."
)

pdf.heading_2("gateway.cmd - Startup Script")
pdf.paragraph(
    "To simplify deployment on Windows systems, gateway.cmd automates server startup:"
)
pdf.code_block(
    "@echo off\n"
    "set \"TMPDIR=C:\\Users\\ASUS\\AppData\\Local\\Temp\"\n"
    "set \"OPENCLAW_GATEWAY_PORT=18789\"\n"
    "openclaw gateway run --port 18789 --force"
)

# ----------------- PAGE 4: PERSONALITY & OPERATION -----------------
pdf.add_page()
pdf.heading_1("4. Customizing Nova's Personality")
pdf.paragraph(
    "Nova's character, rules, and memory are stored under the workspace/ directory. You can edit "
    "these markdown files directly to modify your bot's behavior in real-time."
)

pdf.heading_2("SOUL.md - The Core Personality Blueprint")
pdf.paragraph(
    "Defines the avatar description, name, name style, and conversational guidelines:"
)
pdf.code_block(
    "# SOUL.md - Personality Core\n"
    "\n"
    "- You are a helpful, friendly, and smart personal assistant named Nova.\n"
    "- Chat naturally and keep responses short and conversational."
)

pdf.heading_2("AGENTS.md - Communication Constraints")
pdf.paragraph(
    "Customized rules restrict Nova's message generation to comply with WhatsApp's rendering format:"
)
pdf.code_block(
    "# AGENTS.md - Core Guidelines\n"
    "\n"
    "- Be direct, concise, and helpful.\n"
    "- Respond strictly using WhatsApp messaging format (e.g. bolding text for emphasis).\n"
    "- Avoid markdown tables and HTML tags."
)

pdf.heading_1("5. Steps to Run the Project")
pdf.paragraph(
    "Running this project locally requires starting the AI engine, spawning the gateway, and authenticating."
)
pdf.heading_2("1. Launch Ollama")
pdf.paragraph(
    "Start Ollama on your Windows system. Ensure it is visible in the system tray. "
    "Open terminal and verify the model is downloaded:\n"
    "Command: ollama run llama3.2:1b"
)
pdf.heading_2("2. Start OpenClaw Gateway")
pdf.paragraph(
    "Run gateway.cmd in your main directory. It will start listening on port 18789 "
    "and register connection listeners for your WhatsApp account."
)
pdf.heading_2("3. Connect Dashboard")
pdf.paragraph(
    "To access the graphical Control UI and manage the session, open your browser and navigate to:\n"
    "URL: http://127.0.0.1:18789/?token=eca89116dc38143ce692d733d290850697fe90f11af3a86c\n"
    "If the page requests approval, approve the pairing request in your host terminal."
)

# Save PDF to disk
output_path = r"c:\Users\ASUS\.openclaw\workspace\OpenClaw_WhatsApp_Bot_Documentation.pdf"
pdf.output(output_path)
print(f"PDF Successfully saved to: {output_path}")
