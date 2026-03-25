import sys

path = 'c:/Users/91956/Desktop/resale/product resale system/product/myapp/templates/base.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace :root palette
content = content.replace(
'''        :root {
            /* Fresh Modern Green Palette (No Blue) */
            --brand-primary: #10b981; /* Emerald Green */
            --brand-primary-hover: #059669; /* Darker Emerald */
            --brand-accent: #34d399; /* Light Accent */
            
            --bg-main: #f9fafb;
            --bg-card: #ffffff;''',
'''        :root {
            /* Vibrant Modern Palette (No Blue) */
            --brand-primary: #10b981; /* Emerald Green */
            --brand-primary-hover: #059669; /* Darker Emerald */
            --brand-accent: #34d399; /* Light Accent */
            
            --bg-main: #f0fdf4; /* Fresh Light Mint Body */
            --bg-card: #ffffff;
            
            --bg-header: #111827; /* Dark Slate Header */
            --bg-footer: #111827; /* Dark Slate Footer */
            --text-header: #f9fafb;
            --text-footer: #9ca3af;'''
)

# Add top border to body
content = content.replace(
'''        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background-color: var(--bg-main);
            color: var(--text-main);
            margin: 0;
            padding: 0;
            -webkit-font-smoothing: antialiased;
            letter-spacing: -0.01em;
        }''',
'''        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background-color: var(--bg-main);
            color: var(--text-main);
            margin: 0;
            padding: 0;
            -webkit-font-smoothing: antialiased;
            letter-spacing: -0.01em;
        }'''
)

# Update navbar
content = content.replace(
'''        /* Navbar */
        .marketplace-navbar {
            background-color: var(--bg-card);
            border-bottom: 1px solid var(--border-color);
            padding: 1rem 0;
        }''',
'''        /* Navbar */
        .marketplace-navbar {
            background-color: var(--bg-header);
            border-bottom: 1px solid rgba(255,255,255,0.1);
            padding: 1rem 0;
        }'''
)

# Update search box
content = content.replace(
'''        .search-box {
            display: flex;
            width: 100%;
            background: var(--bg-main);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-sm);
            overflow: hidden;
        }
        .search-box input {
            flex-grow: 1;
            border: none;
            padding: 0.5rem 1rem;
            font-size: 0.95rem;
            background: transparent;
            outline: none;
            color: var(--text-main);
        }
        .search-box input::placeholder {
            color: var(--text-muted);
        }
        .search-box button {
            background: transparent;
            border: none;
            padding: 0 1rem;
            color: var(--text-secondary);
            cursor: pointer;
        }''',
'''        .search-box {
            display: flex;
            width: 100%;
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: var(--radius-sm);
            overflow: hidden;
            transition: border-color 0.2s;
        }
        .search-box:focus-within {
            border-color: var(--brand-primary);
        }
        .search-box input {
            flex-grow: 1;
            border: none;
            padding: 0.5rem 1rem;
            font-size: 0.95rem;
            background: transparent;
            outline: none;
            color: #ffffff;
        }
        .search-box input::placeholder {
            color: #9ca3af;
        }
        .search-box button {
            background: transparent;
            border: none;
            padding: 0 1rem;
            color: #9ca3af;
            cursor: pointer;
        }'''
)

# Update nav-action-item text color
content = content.replace(
'''        .nav-action-item {
            color: var(--text-secondary);''',
'''        .nav-action-item {
            color: var(--text-header);'''
)

# Update category nav
content = content.replace(
'''        /* Category Nav */
        .category-nav {
            background-color: var(--bg-card);
            border-bottom: 1px solid var(--border-color);
            padding: 0.75rem 0;
            overflow-x: auto;
            white-space: nowrap;
        }
        .category-nav::-webkit-scrollbar {
            display: none;
        }
        .category-nav-inner {
            display: flex;
            gap: 1.5rem;
            align-items: center;
        }
        .category-link {
            color: var(--text-secondary);''',
'''        /* Category Nav */
        .category-nav {
            background-color: #1f2937;
            border-bottom: 2px solid var(--brand-primary);
            padding: 0.75rem 0;
            overflow-x: auto;
            white-space: nowrap;
        }
        .category-nav::-webkit-scrollbar {
            display: none;
        }
        .category-nav-inner {
            display: flex;
            gap: 1.5rem;
            align-items: center;
        }
        .category-link {
            color: #d1d5db;'''
)

content = content.replace(
'''<a href="{% url 'product_list' %}" class="category-link fw-bold text-dark">''',
'''<a href="{% url 'product_list' %}" class="category-link fw-bold text-white">'''
)

# Update footer
content = content.replace(
'''        /* Footer */
        .footer-main {
            background-color: var(--bg-card);
            border-top: 1px solid var(--border-color);
            color: var(--text-secondary);
            padding: 3rem 0 1.5rem;
            margin-top: 3rem;
            font-size: 0.9rem;
        }
        .footer-col h6 {
            color: var(--text-main);''',
'''        /* Footer */
        .footer-main {
            background-color: var(--bg-footer);
            border-top: 4px solid var(--brand-primary);
            color: var(--text-footer);
            padding: 3rem 0 1.5rem;
            margin-top: 3rem;
            font-size: 0.9rem;
        }
        .footer-col h6 {
            color: #ffffff;'''
)

content = content.replace(
'''        .footer-bottom {
            border-top: 1px solid var(--border-color);
            padding-top: 1.5rem;
            margin-top: 1.5rem;
            text-align: center;
            color: var(--text-muted);
        }''',
'''        .footer-bottom {
            border-top: 1px solid rgba(255,255,255,0.1);
            padding-top: 1.5rem;
            margin-top: 1.5rem;
            text-align: center;
            color: #6b7280;
        }'''
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Replaced CSS colors successfully")
