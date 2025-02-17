import streamlit as st

from module.languages.pt import resume_pt
from module.languages.en import resume_en
from module.utils import get_badge

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
    language = st.sidebar.selectbox("Choose Language / Escolha o Idioma", ("Português", "English"))

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
    cols = st.columns(4)
    cols[0].write(f"📍 **Location:** {contact_info.get('Location', '')}")
    cols[1].write(f"📞 **Phone:** {contact_info.get('Phone', '')}")
    cols[2].write(f"✉️ **Email:** {contact_info.get('Email', '')}")
    cols[3].write(f"🧑 **Age:** {contact_info.get('Age', '')}")

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
        texto_responsabilidades = 'Responsibilities' if language == "English" else 'Responsabilidades'
        with st.expander(texto_responsabilidades):
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
        st.caption(license)

    # Languages or Idiomas with Flags
    languages_title = "Languages" if language == "English" else "Idiomas"
    st.header(f"🗣️ {languages_title}")
    languages = resume.get("Languages", resume.get("Idiomas", {}))
    for lang, proficiency in languages.items():
        if language == "English":
            flag = "🇧🇷" if lang == "Portuguese" else "🇬🇧" if lang == "English" else "🇪🇸"
        else:
            flag = "🇧🇷" if lang == "Português" else "🇬🇧" if lang == "Inglês" else "🇪🇸"
        st.write(f"{flag} **{lang}:** {proficiency}")

    st.markdown("---")
    st.write("© 2025 João Pedro Almeida Oliveira")
    
    display_sidebar_links()

if __name__ == "__main__":
    main()
