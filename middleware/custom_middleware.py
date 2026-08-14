import logging
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class CustomMiddleware(MiddlewareMixin):
    """
    Custom middleware for hospital management system.
    Handles logging and request/response processing.
    """
    
    def process_request(self, request):
        """Process incoming request"""
        request.custom_data = {
            'timestamp': None,
            'user_role': None,
        }
        
        if request.user.is_authenticated:
            request.custom_data['user_role'] = getattr(request.user, 'role', 'UNKNOWN')
        
        return None
    
    def process_response(self, request, response):
        """Process outgoing response"""
        return response
    
    def process_exception(self, request, exception):
        """Handle exceptions"""
        logger.error(f"Exception in request: {str(exception)}", exc_info=True)
        return None
