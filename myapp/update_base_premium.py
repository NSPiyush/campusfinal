import sys

path = 'c:/Users/91956/Desktop/resale/product resale system/product/myapp/templates/base.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Make the navbar slightly taller and more breathable
content = content.replace(
'''        /* Navbar */
        .marketplace-navbar {
            background-color: var(--bg-header);
            border-bottom: 1px solid rgba(255,255,255,0.1);
            padding: 1rem 0;
        }''',
'''        /* Navbar */
        .marketplace-navbar {
            background-color: var(--bg-header);
            border-bottom: 1px solid rgba(255,255,255,0.05);
            padding: 1.25rem 0;
            box-shadow: 0 4px 20px rgba(0,0,0,0.15);
        }'''
)

# Pill search box
content = content.replace(
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
            padding: 0.5rem 1rem;''',
'''        .search-box {
            display: flex;
            width: 100%;
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 50px; /* Pill shape */
            overflow: hidden;
            transition: all 0.3s ease;
        }
        .search-box:focus-within {
            border-color: var(--brand-primary);
            background: rgba(255,255,255,0.1);
            box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.2);
        }
        .search-box input {
            flex-grow: 1;
            border: none;
            padding: 0.6rem 1.25rem;'''
)
content = content.replace(
'''        .search-box button {
            background: transparent;
            border: none;
            padding: 0 1rem;''',
'''        .search-box button {
            background: transparent;
            border: none;
            padding: 0 1.25rem;'''
)

# Pill buttons
content = content.replace(
'''        .btn-sell {
            background-color: var(--brand-primary);
            color: #ffffff !important;
            padding: 0.4rem 1rem;
            border-radius: var(--radius-sm);''',
'''        .btn-sell {
            background-color: var(--brand-primary);
            color: #ffffff !important;
            padding: 0.5rem 1.5rem;
            border-radius: 50px;'''
)
content = content.replace(
'''        .nav-action-item {
            color: var(--text-header);
            font-weight: 500;
            font-size: 0.95rem;
            display: flex;
            align-items: center;
            gap: 6px;
            cursor: pointer;
            transition: color 0.15s;
        }''',
'''        .nav-action-item {
            color: var(--text-header);
            font-weight: 600;
            font-size: 0.95rem;
            display: flex;
            align-items: center;
            gap: 8px;
            cursor: pointer;
            transition: all 0.2s;
            padding: 0.5rem 0.75rem;
            border-radius: 8px;
        }
        .nav-action-item:hover {
            background: rgba(255,255,255,0.05);
        }'''
)

# Dropdown shadow
content = content.replace(
'''        .custom-dropdown .dropdown-menu {
            margin-top: 0.5rem;
            border: 1px solid var(--border-color);
            box-shadow: var(--shadow-md);
            border-radius: var(--radius-md);''',
'''        .custom-dropdown .dropdown-menu {
            margin-top: 1rem;
            border: 1px solid var(--border-color);
            box-shadow: 0 10px 25px -5px rgba(0,0,0,0.1);
            border-radius: 12px;'''
)

# Replace 'All Categories' in category nav
content = content.replace(
'''<a href="{% url 'product_list' %}" class="category-link fw-bold text-white">All Categories</a>''',
'''<a href="{% url 'product_list' %}" class="category-link fw-bold text-white"><i class="fas fa-bars me-2"></i> All Categories</a>'''
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated base.html with premium formatting")
