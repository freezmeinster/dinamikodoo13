run:
	@odoo
devel:
	@odoo --addons-path=. --database=$(db)  --update=$(modlist)
