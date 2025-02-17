def get_badge(label, color, logo=None):
    if logo:
        return f"![{label}](https://img.shields.io/badge/{label}-{color}?logo={logo}&style=flat)"
    return f"![{label}](https://img.shields.io/badge/{label}-{color}?style=flat)"
