import xmlrpc.client
from django.conf import settings

class OdooClient:
    def __init__(self):
        # 1. Traer credenciales desde settings.py (que las leyó del .env)
        self.url = settings.ODOO_URL
        self.db = settings.ODOO_DB
        self.username = settings.ODOO_USER
        self.password = settings.ODOO_PASSWORD
        
        # 2. Conectar a los endpoints de XML-RPC
        try:
            self.common = xmlrpc.client.ServerProxy(f'{self.url}/xmlrpc/2/common')
            # Autenticar y obtener el ID de usuario (uid)
            self.uid = self.common.authenticate(self.db, self.username, self.password, {})
            self.models = xmlrpc.client.ServerProxy(f'{self.url}/xmlrpc/2/object')
        except Exception as e:
            print(f"Error conectando a Odoo: {e}")
            self.uid = None

    def get_leads(self):
        """Trae los primeros 20 leads"""
        if not self.uid:
            return []
            
        try:
            # Buscar (Search)
            ids = self.models.execute_kw(
                self.db, self.uid, self.password,
                'crm.lead', 'search',
                [[]],  # Filtro vacío = Traer todos
                {'limit': 20}
            )
            # Leer (Read)
            leads = self.models.execute_kw(
                self.db, self.uid, self.password,
                'crm.lead', 'read',
                [ids],
                {'fields': ['name', 'email_from', 'probability', 'stage_id']}
            )
            return leads
        except Exception as e:
            print(f"Error buscando leads: {e}")
            return []

    def create_lead(self, data):
        """Crea un lead nuevo"""
        if not self.uid:
            return None
        
        try:
            lead_id = self.models.execute_kw(
                self.db, self.uid, self.password,
                'crm.lead', 'create',
                [data]
            )
            return lead_id
        except Exception as e:
            print(f"Error creando lead: {e}")
            return None