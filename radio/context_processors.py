def layout_context(request):
    # Example: use a URL query parameter to control layout, default to minimal
    full_layout = request.GET.get('full_layout', 'false') == 'true'
    return {'full_layout': full_layout}
