import streamlit as st

# Function to add badges using Shields.io
def get_badge(label, color, logo=None):
    if logo:
        return f"![{label}](https://img.shields.io/badge/{label}-{color}?logo={logo}&style=flat)"
    return f"![{label}](https://img.shields.io/badge/{label}-{color}?style=flat)"

# Define resume content in English
resume_en = {
    "Personal Information": {
        "Name": "João Pedro Almeida Oliveira",
        "Location": "Belo Horizonte, MG, Brazil",
        "Phone": "+55 31 99370 2136",
        "Email": "Jp080496@gmail.com",
        "LinkedIn": "www.linkedin.com/in/joaopalmeidao"
    },
    "Summary": """
I hold a Bachelor's degree in Business Administration from University FUMEC and a postgraduate degree in Data Science from UNI-BH, both in Belo Horizonte, MG, Brazil.

My career has equipped me with extensive skills in Robotic Process Automation (RPA), programming, and Web Development. I am proficient in using a wide range of Python libraries such as Pandas, Django, Selenium, BS4, regex, boto3, logging, smtplib, imaptools, pyodbc, pymysql, pdfplumber, and more. Additionally, I have a fundamental understanding of JavaScript, HTML5, and CSS3, allowing me to contribute to both front-end and back-end development.

Passionate about leveraging data science for innovative solutions, I am always keen to enhance my knowledge and collaborate on exciting projects. Let's connect and explore opportunities together.
    """,
    "Objective": """
Seeking a challenging position in software development where I can leverage my skills in RPA, Python programming, Web Development, and data science to drive innovative solutions and contribute to the success of the organization.
    """,
    "Experience": [
        {
            "Title": "Software Developer",
            "Company": "Ferreira & Chagas Advogados, Belo Horizonte, MG, Brazil",
            "Duration": "September 2022 – Present (1 Year 11 Months)",
            "Responsibilities": [
                "Developed automations for the legal field.",
                "Developed and implemented Robotic Process Automation (RPA) solutions to streamline legal processes.",
                "Utilized a variety of technologies, including Python, Linux, Apache Airflow, RabbitMQ, MSSQL Server, FastAPI, Flask, Selenium, and BS4.",
                "Created end-to-end automation workflows, reducing manual workload and increasing efficiency.",
                "Collaborated with legal teams to identify automation opportunities and optimize existing processes.",
                "Developed comprehensive documentation and provided training to ensure successful adoption of RPA solutions.",
                "Designed and maintained full-stack web applications, enhancing the firm's digital capabilities."
            ]
        },
        {
            "Title": "Software Developer",
            "Company": "JP SOFTWARES, Belo Horizonte, MG, Brazil",
            "Duration": "October 2021 – Present (2 Years 10 Months)",
            "Responsibilities": [
                "Collaborated on various projects involving Python, Django, Selenium (Python Libraries), SQL, React.js, and JavaScript.",
                "Designed and developed complete web applications, handling both front-end and back-end tasks.",
                "Created automation solutions and a variety of other software applications.",
                "Developed a large-scale Django system using MySQL, ensuring robust performance and scalability."
            ]
        },
        {
            "Title": "IT Administrator",
            "Company": "SUPERMERCADO GUARÁ, Belo Horizonte, MG, Brazil",
            "Duration": "January 2021 – July 2022 (1 Year 7 Months)",
            "Responsibilities": [
                "Implemented Python RPA solutions, transitioning from traditional IT administration to automation-focused roles.",
                "Managed Windows 10 and 7 networks, ensuring smooth operation and security compliance.",
                "Utilized Firebird SQL for database management and integration with automated processes.",
                "Led the migration towards more automated IT operations, improving efficiency and reducing manual workload."
            ]
        },
        {
            "Title": "Administrative Assistant",
            "Company": "SUPERMERCADO GUARÁ, Belo Horizonte, MG, Brazil",
            "Duration": "January 2019 – December 2021 (3 Years)",
            "Responsibilities": [
                "Managed daily administrative tasks, ensuring smooth operation and organization of the office.",
                "Coordinated and scheduled meetings, appointments, and events.",
                "Assisted in inventory management and procurement of office supplies.",
                "Handled customer inquiries and resolved complaints efficiently.",
                "Processed invoices, maintained financial records, and assisted with budget preparation.",
                "Supported the IT department with network maintenance and troubleshooting.",
                "Implemented Python RPA solutions to automate routine tasks, improving efficiency and reducing errors.",
                "Maintained and updated databases using Firebird SQL.",
                "Ensured compliance with company policies and procedures."
            ]
        },
        {
            "Title": "Administrative Assistant",
            "Company": "CNI - Consultoria e Negócios Internacionais Ltda, Belo Horizonte, MG, Brazil",
            "Duration": "July 2017 – November 2017 (5 Months)",
            "Responsibilities": [
                "Collaborated in general administrative support, coordinating daily operations and ensuring efficiency in office functioning.",
                "Assisted in the management of processes related to Agronomy and Rural Financing, facilitating the flow of information and documentation.",
                "Provided support in organizing documents and preparing reports for agricultural projects and rural financing."
            ]
        }
    ],
    "Key Skills": [
        "Python (Programming Language)",
        "Amazon Web Services (AWS)",
        "HTML5",
        "FastAPI",
        "Flask",
        "Dashboards",
        "ETL (Extraction, Transformation, and Loading)",
        "Docker",
        "Linux",
        "Apache Airflow",
        "Debian",
        "Ubuntu",
        "Microsoft SQL Server",
        "Web Scraping",
        "Beautiful Soup",
        "IT Operations",
        "HTML",
        "Git",
        "Front-End Development",
        "Network Installation",
        "Computer Hardware Assembly",
        "Programming",
        "Django",
        "React.js",
        "JavaScript",
        "CSS",
        "Firebase",
        "MongoDB",
        "Computer Maintenance",
        "Customer Relationship Management (CRM)",
        "WebDriver Selenium",
        "Performance Improvement",
        "Operating Systems",
        "Computer Networks",
        "Business Processes",
        "Robotic Process Automation (RPA)",
        "Process Improvement",
        "Automation",
        "XML",
        "Pandas (Software)",
        "Process Automation",
        "Business Process Improvement",
        "Process Optimization",
        "Microsoft PowerPoint",
        "Continuous Process Improvement",
        "Microsoft Word",
        "Microsoft Excel",
        "Big Data Analytics",
        "SQL"
    ],
    "Education": [
        {
            "Degree": "Teaching English as a Second Language",
            "Institution": "St. George International College – Vancouver, Canada",
            "Date": "June 2024"
        },
        {
            "Degree": "Postgraduate Lato Sensu - Specialization in Data Science",
            "Institution": "Centro Universitário de Belo Horizonte",
            "Date": "August 2022 – August 2023"
        },
        {
            "Degree": "Bachelor's Degree in Business Administration",
            "Institution": "Universidade FUMEC",
            "Date": "January 2017 – December 2021"
        },
        {
            "Degree": "Technology Course (CST) in Administration, Business, and Marketing",
            "Institution": "SEBRAE",
            "Date": "January 2015 – December 2016"
        }
    ],
    "Licenses and Certifications": [
        "Machine Learning",
        "Information Security Management (ISO 27001 and 27002)",
        "Data Engineering, Preparation, and Visualization",
        "Infrastructure for Cloud Computing and Big Data",
        "Project Management Methodology",
        "Apache Airflow: Data Extraction",
        "Apache Airflow: Data Transformation with Spark",
        "A Deep Dive into Airflow: Kubernetes Executor",
        "Python: Advancing in Object-Oriented Programming",
        "Microservices in Practice: Messaging with RabbitMQ",
        "Getting Started with Flask: Python Web Framework",
        "Flask: Advancing in Web Development with Python",
        "Flask: Building a Web App with Python",
        "Python: Understanding Object-Oriented Programming",
        "Docker: Creating and Managing Containers",
        "Apache Airflow: Orchestrating Your First Data Pipeline",
        "Linux Onboarding: Using the CLI Efficiently",
        "Python Pandas: Advanced Techniques",
        "Python for Data Science: Language and Numpy",
        "SQL Server: Advanced Queries with Microsoft SQL Server 2017",
        "Python for Data Science: Functions, Packages, and Pandas",
        "Spark: Introducing the Tool",
        "Python String: Extracting Information from a URL",
        "Deep Dive into Airflow: Local and Celery Executors",
        "Python Pandas: Handling and Analyzing Data",
        "Scraping with Python: Web Data Collection",
        "Python 3 Course from Basic to Advanced with Django, Selenium, Regex, Tests and TDD, OOP, Design Patterns GoF, Algorithms, and more",
        "JavaScript and TypeScript from Basic to Advanced (146 hours) - Udemy (ongoing)"
    ],
    "Languages": {
        "Portuguese": "Native",
        "English": "Advanced",
        "Spanish": "Basic"
    }
}

# Define resume content in Portuguese
resume_pt = {
    "Informações Pessoais": {
        "Nome": "João Pedro Almeida Oliveira",
        "Location": "Belo Horizonte, MG, Brasil",
        "Phone": "+55 31 99370 2136",
        "Email": "Jp080496@gmail.com",
        "LinkedIn": "www.linkedin.com/in/joaopalmeidao"
    },
    "Resumo": """
Possuo Bacharelado em Administração de Empresas pela Universidade FUMEC e pós-graduação em Ciência de Dados pela UNI-BH, ambas em Belo Horizonte, MG, Brasil.

Minha carreira me proporcionou amplas habilidades em Automação de Processos Robóticos (RPA), programação e Desenvolvimento Web. Sou proficiente no uso de diversas bibliotecas Python como Pandas, Django, Selenium, BS4, regex, boto3, logging, smtplib, imaptools, pyodbc, pymysql, pdfplumber, entre outras. Além disso, tenho compreensão fundamental de JavaScript, HTML5 e CSS3, permitindo-me contribuir tanto para o desenvolvimento front-end quanto back-end.

Apaixonado por alavancar a ciência de dados para soluções inovadoras, estou sempre disposto a aprimorar meus conhecimentos e colaborar em projetos empolgantes. Vamos nos conectar e explorar oportunidades juntos.
    """,
    "Objetivo": """
Buscar uma posição desafiadora em desenvolvimento de software onde eu possa aproveitar minhas habilidades em RPA, programação Python, Desenvolvimento Web e ciência de dados para impulsionar soluções inovadoras e contribuir para o sucesso da organização.
    """,
    "Experiência": [
        {
            "Title": "Desenvolvedor de Software",
            "Company": "Ferreira & Chagas Advogados, Belo Horizonte, MG, Brasil",
            "Duration": "Setembro 2022 – Presente (1 Ano 11 Meses)",
            "Responsibilities": [
                "Desenvolvi automações para o campo jurídico.",
                "Desenvolvi e implementei soluções de Automação de Processos Robóticos (RPA) para otimizar processos jurídicos.",
                "Utilizei diversas tecnologias, incluindo Python, Linux, Apache Airflow, RabbitMQ, MSSQL Server, FastAPI, Flask, Selenium e BS4.",
                "Criei fluxos de trabalho de automação de ponta a ponta, reduzindo a carga de trabalho manual e aumentando a eficiência.",
                "Colaborei com equipes jurídicas para identificar oportunidades de automação e otimizar processos existentes.",
                "Desenvolvi documentação abrangente e forneci treinamento para garantir a adoção bem-sucedida das soluções de RPA.",
                "Projetei e mantive aplicações web full-stack, aprimorando as capacidades digitais do escritório."
            ]
        },
        {
            "Title": "Desenvolvedor de Software",
            "Company": "JP SOFTWARES, Belo Horizonte, MG, Brasil",
            "Duration": "Outubro 2021 – Presente (2 Anos 10 Meses)",
            "Responsibilities": [
                "Colaborei em vários projetos envolvendo Python, Django, Selenium (Bibliotecas Python), SQL, React.js e JavaScript.",
                "Projetei e desenvolvi aplicações web completas, lidando com tarefas de front-end e back-end.",
                "Criei soluções de automação e uma variedade de outras aplicações de software.",
                "Desenvolvi um sistema Django de grande escala usando MySQL, garantindo desempenho robusto e escalabilidade."
            ]
        },
        {
            "Title": "Administrador de TI",
            "Company": "SUPERMERCADO GUARÁ, Belo Horizonte, MG, Brasil",
            "Duration": "Janeiro 2021 – Julho 2022 (1 Ano 7 Meses)",
            "Responsibilities": [
                "Implementei soluções de RPA em Python, fazendo a transição de administração de TI tradicional para funções focadas em automação.",
                "Gerenciei redes Windows 10 e 7, garantindo operação suave e conformidade de segurança.",
                "Utilizei Firebird SQL para gerenciamento de banco de dados e integração com processos automatizados.",
                "Liderei a migração para operações de TI mais automatizadas, melhorando a eficiência e reduzindo a carga de trabalho manual."
            ]
        },
        {
            "Title": "Assistente Administrativo",
            "Company": "SUPERMERCADO GUARÁ, Belo Horizonte, MG, Brasil",
            "Duration": "Janeiro 2019 – Dezembro 2021 (3 Anos)",
            "Responsibilities": [
                "Gerenciei tarefas administrativas diárias, garantindo operação suave e organização do escritório.",
                "Coordenei e agendei reuniões, compromissos e eventos.",
                "Auxiliei na gestão de inventário e na aquisição de suprimentos de escritório.",
                "Atendi consultas de clientes e resolvi reclamações de forma eficiente.",
                "Processamento de faturas, manutenção de registros financeiros e assistência na preparação de orçamentos.",
                "Apoiei o departamento de TI com manutenção de rede e solução de problemas.",
                "Implementei soluções de RPA em Python para automatizar tarefas rotineiras, melhorando a eficiência e reduzindo erros.",
                "Mantive e atualizei bancos de dados usando Firebird SQL.",
                "Garanti conformidade com as políticas e procedimentos da empresa."
            ]
        },
        {
            "Title": "Assistente Administrativo",
            "Company": "CNI - Consultoria e Negócios Internacionais Ltda, Belo Horizonte, MG, Brasil",
            "Duration": "Julho 2017 – Novembro 2017 (5 Meses)",
            "Responsibilities": [
                "Colaborei no suporte administrativo geral, coordenando operações diárias e garantindo eficiência no funcionamento do escritório.",
                "Auxiliei na gestão de processos relacionados à Agronomia e Financiamento Rural, facilitando o fluxo de informações e documentação.",
                "Forneci suporte na organização de documentos e na preparação de relatórios para projetos agrícolas e financiamento rural."
            ]
        }
    ],
    "Habilidades Principais": [
        "Python (Linguagem de Programação)",
        "Amazon Web Services (AWS)",
        "HTML5",
        "FastAPI",
        "Flask",
        "Dashboards",
        "ETL (Extração, Transformação e Carregamento)",
        "Docker",
        "Linux",
        "Apache Airflow",
        "Debian",
        "Ubuntu",
        "Microsoft SQL Server",
        "Web Scraping",
        "Beautiful Soup",
        "Operações de TI",
        "HTML",
        "Git",
        "Desenvolvimento Front-End",
        "Instalação de Redes",
        "Montagem de Hardware de Computador",
        "Programação",
        "Django",
        "React.js",
        "JavaScript",
        "CSS",
        "Firebase",
        "MongoDB",
        "Manutenção de Computadores",
        "Gestão de Relacionamento com o Cliente (CRM)",
        "WebDriver Selenium",
        "Melhoria de Desempenho",
        "Sistemas Operacionais",
        "Redes de Computadores",
        "Processos de Negócios",
        "Automação de Processos Robóticos (RPA)",
        "Melhoria de Processos",
        "Automação",
        "XML",
        "Pandas (Software)",
        "Automação de Processos",
        "Melhoria de Processos de Negócios",
        "Otimização de Processos",
        "Microsoft PowerPoint",
        "Melhoria Contínua de Processos",
        "Microsoft Word",
        "Microsoft Excel",
        "Análise de Big Data",
        "SQL"
    ],
    "Educação": [
        {
            "Degree": "Ensino de Inglês como Segunda Língua",
            "Institution": "St. George International College – Vancouver, Canadá",
            "Date": "Junho 2024"
        },
        {
            "Degree": "Pós-graduação Lato Sensu - Especialização em Ciência de Dados",
            "Institution": "Centro Universitário de Belo Horizonte",
            "Date": "Agosto 2022 – Agosto 2023"
        },
        {
            "Degree": "Bacharelado em Administração de Empresas",
            "Institution": "Universidade FUMEC",
            "Date": "Janeiro 2017 – Dezembro 2021"
        },
        {
            "Degree": "Curso de Tecnologia (CST) em Administração, Negócios e Marketing",
            "Institution": "SEBRAE",
            "Date": "Janeiro 2015 – Dezembro 2016"
        }
    ],
    "Licenças e Certificações": [
        "Machine Learning",
        "Gestão de Segurança da Informação (ISO 27001 e 27002)",
        "Engenharia de Dados, Preparação e Visualização",
        "Infraestrutura para Computação em Nuvem e Big Data",
        "Metodologia de Gestão de Projetos",
        "Apache Airflow: Extração de Dados",
        "Apache Airflow: Transformação de Dados com Spark",
        "Um Mergulho Profundo no Airflow: Executor Kubernetes",
        "Python: Avançando em Programação Orientada a Objetos",
        "Microserviços na Prática: Mensageria com RabbitMQ",
        "Introdução ao Flask: Framework Web Python",
        "Flask: Avançando no Desenvolvimento Web com Python",
        "Flask: Construindo uma Aplicação Web com Python",
        "Python: Compreendendo Programação Orientada a Objetos",
        "Docker: Criando e Gerenciando Containers",
        "Apache Airflow: Orquestrando Seu Primeiro Pipeline de Dados",
        "Linux Onboarding: Usando o CLI de Forma Eficiente",
        "Python Pandas: Técnicas Avançadas",
        "Python para Ciência de Dados: Linguagem e Numpy",
        "SQL Server: Consultas Avançadas com Microsoft SQL Server 2017",
        "Python para Ciência de Dados: Funções, Pacotes e Pandas",
        "Spark: Introdução à Ferramenta",
        "Python String: Extraindo Informações de uma URL",
        "Mergulho Profundo no Airflow: Executors Local e Celery",
        "Python Pandas: Manipulando e Analisando Dados",
        "Scraping com Python: Coleta de Dados da Web",
        "Curso de Python 3 do Básico ao Avançado com Django, Selenium, Regex, Testes e TDD, POO, Padrões de Design GoF, Algoritmos e mais",
        "JavaScript e TypeScript do Básico ao Avançado (146 horas) - Udemy (em andamento)"
    ],
    "Idiomas": {
        "Português": "Nativo",
        "Inglês": "Avançado",
        "Espanhol": "Básico"
    }
}

def display_sidebar_links():

    LINKS_OUTROS_SITES = {
        'GitHub': 'https://github.com/joaopalmeidao',
        'LinkedIn': 'https://www.linkedin.com/in/joaopalmeidao/',
    }

    st.sidebar.markdown(
    """
    <style>
        .dropdown {
            position: relative;
            display: inline-block;
        }
        .dropdown-content {
            display: none;
            position: absolute;
            background-color: #f9f9f9;
            min-width: 160px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
        }
        .dropdown:hover .dropdown-content {
            display: block;
        }
        .dropdown-item {
            padding: 12px 16px !important;
            display: block !important;
            text-decoration: none !important;
            color: #0080ff !important;
            border-radius: 10px;
        }
        .dropdown-item:hover {
            background-color: #ddd;
        }
    </style>
    """
    , unsafe_allow_html=True
    )

    st.sidebar.markdown("<div class='dropdown'>", unsafe_allow_html=True)
    st.sidebar.markdown("  <div class='dropdown-content'>", unsafe_allow_html=True)

    
    for name, link in LINKS_OUTROS_SITES.items():
        st.sidebar.markdown(f"    <a class='dropdown-item' target='_blank' href='{link}'>{name}</a>", unsafe_allow_html=True)

    st.sidebar.markdown("  </div>", unsafe_allow_html=True)
    st.sidebar.markdown("</div>", unsafe_allow_html=True)

# Streamlit App
def main():
    st.set_page_config(page_title="João Pedro Almeida Oliveira - Resume", layout="wide")

    # Custom CSS for badges and icons
    st.markdown("""
    <style>
    .section-title {
        display: flex;
        align-items: center;
    }
    .section-title img {
        margin-right: 10px;
    }
    .badge {
        display: inline-block;
        padding: 0.25em 0.4em;
        font-size: 75%;
        font-weight: 700;
        line-height: 1;
        text-align: center;
        white-space: nowrap;
        vertical-align: baseline;
        border-radius: 0.25rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # Sidebar for language selection
    st.sidebar.title("Language / Idioma")
    language = st.sidebar.selectbox("Choose Language / Escolha o Idioma", ("English", "Português"))

    # Select resume content based on language
    if language == "English":
        resume = resume_en
    else:
        resume = resume_pt

    # Display Personal Information with Icons
    name = resume.get("Personal Information", resume.get("Informações Pessoais", {})).get("Name", "Resume")
    st.title(f"👤 {name}")

    # Contact Information with Icons
    contact_info = resume.get("Personal Information", resume.get("Informações Pessoais", {}))
    cols = st.columns(3)
    cols[0].write(f"📍 **Location:** {contact_info.get('Location', '')}")
    cols[1].write(f"📞 **Phone:** {contact_info.get('Phone', '')}")
    cols[2].write(f"✉️ **Email:** {contact_info.get('Email', '')}")
    st.markdown(f"🔗 **LinkedIn:** [{contact_info.get('LinkedIn', '')}]({contact_info.get('LinkedIn', '')})")

    st.markdown("---")

    # Summary or Resumo
    summary_title = "Summary" if language == "English" else "Resumo"
    st.header(f"📄 {summary_title}")
    st.write(resume.get("Summary", resume.get("Resumo", "")))

    # Objective or Objetivo
    objective_title = "Objective" if language == "English" else "Objetivo"
    st.header(f"🎯 {objective_title}")
    st.write(resume.get("Objective", resume.get("Objetivo", "")))

    # Experience or Experiência
    experience_title = "Experience" if language == "English" else "Experiência"
    st.header(f"💼 {experience_title}")
    for job in resume.get("Experience", resume.get("Experiência", [])):
        job_title = job.get('Title', '')
        company = job.get('Company', '')
        duration = job.get('Duration', '')
        st.subheader(f"🔹 {job_title} at {company}")
        st.write(f"**Duration:** {duration}")
        with st.expander("Responsibilities"):
            for responsibility in job.get("Responsibilities", []):
                st.markdown(f"- {responsibility}")
        st.write("")

    # Key Skills or Habilidades Principais with Badges
    skills_title = "Key Skills" if language == "English" else "Habilidades Principais"
    st.header(f"🛠️ {skills_title}")
    skills = resume.get("Key Skills", resume.get("Habilidades Principais", []))
    # Display skills as badges using Shields.io
    skills_badges = [get_badge(skill.replace(' ', '%20'), 'blue') for skill in skills]
    st.markdown(" ".join(skills_badges))

    # Education or Educação
    education_title = "Education" if language == "English" else "Educação"
    st.header(f"🎓 {education_title}")
    for edu in resume.get("Education", resume.get("Educação", [])):
        degree = edu.get('Degree', '')
        institution = edu.get('Institution', '')
        date = edu.get('Date', '')
        st.subheader(f"📚 {degree}")
        st.write(f"**Institution:** {institution}")
        st.write(f"**Date:** {date}")
        st.write("")

    # Licenses and Certifications or Licenças e Certificações with Expanders
    licenses_title = "Licenses and Certifications" if language == "English" else "Licenças e Certificações"
    st.header(f"📜 {licenses_title}")
    licenses = resume.get("Licenses and Certifications", resume.get("Licenças e Certificações", []))
    for license in licenses:
        with st.expander(license):
            st.write("")

    # Languages or Idiomas with Flags
    languages_title = "Languages" if language == "English" else "Idiomas"
    st.header(f"🗣️ {languages_title}")
    languages = resume.get("Languages", resume.get("Idiomas", {}))
    for lang, proficiency in languages.items():
        flag = "🇧🇷" if lang == "Portuguese" else "🇬🇧" if lang == "English" else "🇪🇸"
        st.write(f"{flag} **{lang}:** {proficiency}")

    st.markdown("---")
    st.write("© 2025 João Pedro Almeida Oliveira")
    
    display_sidebar_links()

if __name__ == "__main__":
    main()
