from rest_framework.views import APIView
from rest_framework.response import Response
from .services import OdooClient

class LeadList(APIView):
    def get(self, request):
        """Devuelve la lista de oportunidades desde Odoo"""
        odoo = OdooClient()
        leads = odoo.get_leads()
        return Response(leads)

    def post(self, request):
        """Crea una nueva oportunidad en Odoo"""
        odoo = OdooClient()
        data = request.data  # Datos que vienen del Frontend
        
        # Validación básica
        if not data.get('name'):
            return Response({"error": "Falta el nombre de la oportunidad"}, status=400)
            
        new_id = odoo.create_lead(data)
        
        if new_id:
            return Response({"message": "Lead creado", "id": new_id})
        else:
            return Response({"error": "No se pudo crear en Odoo"}, status=500)