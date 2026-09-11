from flask import session


TRANSLATIONS = {
    "en": {
        "jobs": "Jobs",
        "about": "About",
        "add_job": "Add Job",
        "my_jobs": "My Jobs",
        "profile": "Profile",
        "logout": "Logout",
        "login": "Login",
        "register": "Register",

        "hero_eyebrow": "Your next career move starts here",
        "hero_title_line_1": "Find work that",
        "hero_title_line_2": "moves you forward.",
        "hero_text": (
            "Discover opportunities from growing companies "
            "across different industries and locations."
        ),

        "search": "Search",
        "search_placeholder": "Job title, company...",
        "category": "Category",
        "all_categories": "All Categories",
        "location": "Location",
        "location_placeholder": "e.g. Tbilisi",
        "sort": "Sort",
        "newest": "Newest",
        "oldest": "Oldest",
        "search_jobs": "Search Jobs",
        "reset": "Reset",

        "latest_opportunities": "Latest Opportunities",
        "job_found": "job found",
        "jobs_found": "jobs found",

        "posted_by": "Posted by",
        "view_job": "View Job",

        "no_matching_jobs": "No matching jobs",
        "no_matching_jobs_text": (
            "Try changing your search filters "
            "or browse all available vacancies."
        ),
        "view_all_jobs": "View All Jobs",

        "footer_text": "Find opportunities. Build careers.",
    },

    "ka": {
        "jobs": "ვაკანსიები",
        "about": "ჩვენ შესახებ",
        "add_job": "ვაკანსიის დამატება",
        "my_jobs": "ჩემი ვაკანსიები",
        "profile": "პროფილი",
        "logout": "გასვლა",
        "login": "შესვლა",
        "register": "რეგისტრაცია",

        "hero_eyebrow": "შენი კარიერის შემდეგი ნაბიჯი აქ იწყება",
        "hero_title_line_1": "იპოვე სამსახური,",
        "hero_title_line_2": "რომელიც წინ წაგიყვანს.",
        "hero_text": (
            "აღმოაჩინე შესაძლებლობები სხვადასხვა სფეროსა "
            "და ლოკაციაზე მოქმედ კომპანიებში."
        ),

        "search": "ძიება",
        "search_placeholder": "ვაკანსია, კომპანია...",
        "category": "კატეგორია",
        "all_categories": "ყველა კატეგორია",
        "location": "ლოკაცია",
        "location_placeholder": "მაგ. თბილისი",
        "sort": "დალაგება",
        "newest": "უახლესი",
        "oldest": "უძველესი",
        "search_jobs": "ვაკანსიების ძიება",
        "reset": "გასუფთავება",

        "latest_opportunities": "უახლესი ვაკანსიები",
        "job_found": "ვაკანსია მოიძებნა",
        "jobs_found": "ვაკანსია მოიძებნა",

        "posted_by": "ავტორი",
        "view_job": "ვაკანსიის ნახვა",

        "no_matching_jobs": "ვაკანსია ვერ მოიძებნა",
        "no_matching_jobs_text": (
            "შეცვალე ძიების პარამეტრები ან "
            "ნახე ყველა ხელმისაწვდომი ვაკანსია."
        ),
        "view_all_jobs": "ყველა ვაკანსიის ნახვა",

        "footer_text": "იპოვე შესაძლებლობა. განავითარე კარიერა.",
    },
}


CATEGORY_TRANSLATIONS = {
    "IT": {
        "en": "IT",
        "ka": "IT",
    },
    "Design": {
        "en": "Design",
        "ka": "დიზაინი",
    },
    "Marketing": {
        "en": "Marketing",
        "ka": "მარკეტინგი",
    },
    "Finance": {
        "en": "Finance",
        "ka": "ფინანსები",
    },
    "Sales": {
        "en": "Sales",
        "ka": "გაყიდვები",
    },
    "Human Resources": {
        "en": "Human Resources",
        "ka": "ადამიანური რესურსები",
    },
    "Customer Service": {
        "en": "Customer Service",
        "ka": "მომხმარებელთა მომსახურება",
    },
    "Operations": {
        "en": "Operations",
        "ka": "ოპერაციები",
    },
    "Other": {
        "en": "Other",
        "ka": "სხვა",
    },
}


def get_language():
    language = session.get(
        "language",
        "en",
    )

    if language not in TRANSLATIONS:
        return "en"

    return language


def t(key):
    language = get_language()

    return TRANSLATIONS.get(
        language,
        TRANSLATIONS["en"],
    ).get(
        key,
        key,
    )


def translate_category(category_name):
    language = get_language()

    translations = CATEGORY_TRANSLATIONS.get(
        category_name
    )

    if not translations:
        return category_name

    return translations.get(
        language,
        category_name,
    )