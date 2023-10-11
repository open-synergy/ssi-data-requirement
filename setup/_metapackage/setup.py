import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-data-requirement",
    description="Meta package for open-synergy-ssi-data-requirement Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_data_requirement_google_drive',
        'odoo14-addon-ssi_data_requirement_project',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
