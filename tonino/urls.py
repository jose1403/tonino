from django.conf.urls import include, url
from django.contrib import admin
from nucleo import views as nucleo_app
from gestion import views as gestion_app
from rubro import views as rubro, rubro_pdf
from proovedores import views as proovedores, proovedor_pdf
from contabilidad import views as contabilidad
from recepcion import views as recepcion, recepcion_pdf, filtro_de_recepciones as filtroR
from clientes import views as cliente, clientes_pdf
from despacho import views as despacho,filtro_de_despachos as filtroD, despacho_pdf
from plantas import views as plantas_app
from ajax_select import urls as ajax_select_urls
import settings
urlpatterns = [

    # Examples:
    # url(r'^$', 'tonino.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS

    url(r'^ajax_select/', include(ajax_select_urls)),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^chaining/', include('smart_selects.urls')),\
    url(r'^generar_pdf/(?P<pk>.*)/$', recepcion.generar_pdf, name='generar-pdf'),
    url(r'^generar_csv/$', rubro.rubro_csv, name='generar-csv'),

  
    url(r'^media/(?P<path>.*)','django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    #url(r'^create',  view='views.create',name='create'),
   # url(r'^ajax_lookup/(?P<channel>[-\w]+)$', 'ajax_select.views.ajax_lookup', name = 'ajax_lookup'),



    url(r'^$', nucleo_app.inicio_prinsipal),
    url(r'^base/$',nucleo_app.Sitio_Base, name='base' ),
    url(r'^accounts/login/$',nucleo_app.login, name='login'),
    url(r'^accounts/logout/$',nucleo_app.logout, name='logout'),
    url(r'^buscador/$',gestion_app.buscador, name='buscador'),


    url(r'^delete/model/$', rubro.delete_model, name='delete'),

    url(r'^agregado/$', nucleo_app.agregado, name='agregado' ),
    url(r'^agregado/nuevo/$', nucleo_app.proceso,  name='agregado-nuevo'),
    url(r'^agregado/rubro/ver/$',rubro.Mostrar_Rubros, name='ver-rubro'),
    url(r'^agregado/rubro/agregar/$',rubro.Agregar_Rubros, name='add-rubro'),
    url(r'^agregado/rubro/editar/(?P<pk>.*)/$', rubro.Editar_Rubro, name='edit-rubro'),
    url(r'^agregado/rubro/generar-csv/(?P<pk>.*)/$', rubro.rubro_id_csv, name='rubro-pdf'),

    url(r'^agregado/rubro/ver/csv/$', rubro.rubro_csv, name='lsta-rubro-csv'),
    url(r'^agregado/rubro/ver/pdf/$', rubro_pdf.rubro_pdf, name='lsta-rubro-pdf'),



    url(r'^agregado/rubro/(?P<pk>.*)/variedades/ver/$',rubro.Rubro_Variedades_Ver, name='ver-rubro-variedades'),

    url(r'^agregado/rubro/(?P<pk>.*)/variedades/agregar/$',rubro.Rubro_Variedades_Add, name='add-rubro-variedades'),
    url(r'^agregado/rubro/(?P<pkrubro>.*)/variedades/edit/(?P<pkvariedad>.*)/$',rubro.Rubro_Variedades_Edit, name='edit-rubro-variedades'),


    url(r'^agregado/rubro/(?P<pk>.*)/tipo/ver/$',rubro.Rubro_Tipo_Ver, name='ver-rubro-tipo'),
    url(r'^agregado/rubro/(?P<pk>.*)/tipo/agregar/$',rubro.Rubro_Tipo_Add, name='add-rubro-tipo'),
    url(r'^agregado/rubro/(?P<pkrubro>.*)/tipo/edit/(?P<pktipo>.*)/$',rubro.Rubro_Tipo_Edit, name='edit-rubro-tipo'),


    url(r'^agregado/plantas/ver/$',plantas_app.Ver_Plantas, name='ver-plantas'),
    url(r'^agregado/plantas/agregar/$',plantas_app.Add_Plantas, name='add-plantas'),
    url(r'^agregado/plantas/edit/(?P<pk>.*)/$', plantas_app.Edit_Plantas, name='edit-plantas'),

    url(r'^agregado/plantas/(?P<pk>.*)/silos/ver/$',plantas_app.Ver_Silos, name='ver-silos'),
    url(r'^agregado/plantas/(?P<pk>.*)/silos/add/$',plantas_app.Add_Silos, name='add-silos'),

    url(r'^agregado/plantas/(?P<pkplanta>.*)/silos/edit/(?P<pksilo>.*)/$', plantas_app.Edit_Silos, name='edit-silos'),


    url(r'^agregado/proovedor/ver/$', proovedores.Ver_Productor,{'valor':True}, name='ver-productor'),
    url(r'^prueva/$', proovedor_pdf.convertir_pdf, name='prueva'),

    url(r'^agregado/proovedor/ver/desabilitados/$', proovedores.Ver_Productor,{'valor':False}, name='ver-productor-des'),
    url(r'^agregado/proovedor/ver/cvs/$', proovedores.lista_productores_csv, name='productores-lista-cvs'),

    url(r'^agregado/proovedor/ver/pdf/$', proovedor_pdf.lista_productores_pdf, name='productores-lista-pdf'),

    url(r'^agregado/proovedor/add/$', proovedores.Add_Productor, name='add-productor'),
    url(r'^agregado/rubro-proovedor/edit/(?P<pk>.*)/$',proovedores.Rubro_Productor_Edit, name='edit-productor'),
    url(r'^agregado/rubro-proovedor/generar/pdf/(?P<pk>.*)/$',proovedor_pdf.info_productor_pdf, name='productor-info-pdf'),

    
    url(r'^agregado/proovedor/(?P<pk>.*)/zona/ver/$', proovedores.Ver_Zonas_Productor, name='ver-zonas-productor'),
    url(r'^agregado/proovedor/(?P<pk>.*)/zona/add/$', proovedores.Add_Zonas_Productor, name='add-zonas-productor'),
    url(r'^agregado/proovedor/(?P<pkpro>.*)/zona/(?P<pkzona>.*)/$',proovedores.Edit_Zona_Productor, name='edit-zonas-productor'),
    url(r'^agregado/rubro-proovedor/zona/generar/pdf/(?P<pk>.*)/$',proovedor_pdf.info_zona_productor_pdf, name='productor-info-zona-pdf'),



    #00000000000000000000000000000000000000000000000000000
    url(r'^agregado/contabilidad/$', contabilidad.Contabilidad, name='contabilidad'),
    url(r'^agregado/bancos/ver/$', contabilidad.Ver_Bancos, name='ver-bancos'),
    url(r'^agregado/bancos/add/$', contabilidad.Add_Bancos, name='add-bancos'),
    url(r'^agregado/bancos/edit/(?P<pk>.*)/$', contabilidad.Edit_Bancos, name='edit-bancos'),

    url(r'^agregado/bancos/tipo-cuenta/ver/$', contabilidad.Ver_Tipo_Cuenta, name='ver-tipo-cuenta'),
    url(r'^agregado/bancos/tipo-cuenta/add/$', contabilidad.Add_Tipo_Cuenta, name='add-tipo-cuenta'),
    url(r'^agregado/bancos/tipo-cuenta/edit/(?P<pk>.*)/$', contabilidad.Edit_Tipo_Cuenta, name='edit-tipo-cuenta'),


    url(r'^agregado/ciclo/ver/$', contabilidad.Ver_Ciclos, name='ver-ciclos'),
    url(r'^agregado/ciclo/ver/desabilitados/$', contabilidad.Ver_Ciclos_Des, name='ver-ciclos-des'),

    url(r'^agregado/ciclo/add/$', contabilidad.Add_Ciclos, name='add-ciclos'),
    url(r'^agregado/ciclo/edit/(?P<pk>.*)/$', contabilidad.Edit_Ciclos, name='edit-ciclos'),

    url(r'^agregado/ciclo/(?P<pk>.*)/precios/ver/$', contabilidad.Ver_PresioXCiclo, name='ver-presiox-ciclo'),
    url(r'^agregado/ciclo/precios/ver/(?P<nciclo>.*)/$', contabilidad.Ver_Presio_Ciclo, name='ver-presio-ciclo'),

    url(r'^agregado/ciclo/(?P<pk>.*)/precios/add/$', contabilidad.Add_PresioXCiclo, name='add-presiox-ciclo'),
    
    url(r'^agregado/ciclo/(?P<pkciclo>.*)/precios/edit/(?P<pkprecio>.*)/$', contabilidad.Edit_PresioXCiclo, name='edit-presiox-ciclo'),
    url(r'^agregado/contabilidad/gananciasdelciclo/(?P<pk>.*)/$', nucleo_app.GananciasDelCiclo, name='ganacias-del-ciclo'),
    url(r'^agregado/contabilidad/ganancias-del-ciclo/(?P<pkciclo>.*)/rubro/(?P<pkrubro>.*)/$', nucleo_app.GananciasDelCicloXRubro, name='ganacias-del-cicloX-rubro'),


    

    #=======================================================================

    url(r'^agregado/recepcion/ver/$', recepcion.Mostrar_Recepcion.as_view(), name='ver-recepcion'),
    url(r'^agregado/recepcion/add/$', recepcion.Add_Recepcion, name='add-recepcion'),
    url(r'^agregado/recepcion/edit/(?P<pk>.*)/$', recepcion.Edit_Recepcion, name='edit-recepcion'),

    url(r'^agregado/recepcion/pago/add/$', recepcion.Add_Pago_Recepcion, name='add-pago-recepcion'),
    url(r'^agregado/recepcion/total-pago/add/$', recepcion.Add_Total_Recepcion, name='add-total-recepcion'),
    url(r'^agregado/recepcion/factura/(?P<pk>.*)/', recepcion.Ver_Factura_Recepcion, name='factura-recepcion'),
    url(r'^agregado/recepcion/generar_pdf/(?P<pk>.*)/', recepcion_pdf.factura_recepcion_pdf, name='factura-recepcion-pdf'),
    url(r'^agregado/recepcion/rubro/(?P<nombre>[A-Za-z].*)/(?P<pk>.*)/', recepcion.cantidad_ingresada_a_silo, name='cantidad_ingresada'),


    url(r'^agregado/recepcion/(?P<year>\d{4})/$', filtroR.RecepcionesAnuales.as_view(), name='recepciones_anuales'),
    url(r'^agregado/recepcion/(?P<year>\d{4})/(?P<month>\d{2})/$', filtroR.RecepcionesMes.as_view(), name='recepciones_mensuales'),
    url(r'^agregado/recepcion/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',filtroR.RecepcionesDiarias.as_view(), name='recepciones_diarias'),
    #url(r'^agregado/recepcion/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<pk>.*)$',filtroR.Recepciones, name='lista_recepciones'),
    url(r'^prueva-ajax/$', recepcion.prueva_ajax, name='ver-ajax'),

    url(r'^agregado/cuentas/(?P<year>\d{4})/$', filtroR.CuentasAnuales.as_view(), name='cuentas_anuales'),
    url(r'^agregado/cuentas/(?P<year>\d{4})/(?P<month>\d{2})/$', filtroR.CuentasMensuales.as_view(), name='cuentas_mensuales'),
    url(r'^agregado/cuentas/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', filtroR.CuentasDiarias.as_view(), name='cuentas_diarias'),
   

    url(r'^agregado/cuentas/ver/$', recepcion.Mostrar_CuetasXpagar.as_view(), name='ver-cuentasx-pagar'),
    url(r'^agregado/cuentas/edit/(?P<pk>.*)/$', recepcion.Editar_CuentasXpagar, name='edit-cuentasx-pagar'),



    url(r'^agregado/cliente/ver/$', cliente.Ver_Cliente, name='ver-cliente'),
    url(r'^agregado/cliente/ver/cvs/$', cliente.lista_clientes_csv, name='clientes-lista-cvs'),
    url(r'^agregado/cliente/ver/pdf/$', clientes_pdf.lista_clientes_pdf, name='clientes-lista-pdf'),

    url(r'^agregado/cliente/add/$', cliente.Add_Cliente, name='add-cliente'),
    url(r'^agregado/cliente/edit/(?P<pk>.*)/$', cliente.Edit_Cliente, name='edit-cliente'),
    url(r'^agregado/cliente/generar/pdf/(?P<pk>.*)/$',clientes_pdf.info_cliente_pdf, name='cliente-info-pdf'),


    url(r'^agregado/despacho/ver/$', despacho.Mostrar_Despacho.as_view(), name='ver-despacho'),
    url(r'^agregado/despacho/add/$', despacho.Add_Despacho, name='add-despacho'),

    url(r'^agregado/despacho/(?P<year>\d{4})/$', filtroD.DespachosAnuales.as_view(), name='despachos_anuales'),
    url(r'^agregado/despacho/(?P<year>\d{4})/(?P<month>\d{2})/$', filtroD.DespachosMes.as_view(), name='despachos_mensuales'),
    url(r'^agregado/despacho/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',filtroD.DespachosDiarios.as_view(), name='despachos_diarios'),

    url(r'^agregado/despacho/factura/(?P<pk>.*)/', despacho.Ver_Factura_Despacho, name='factura-despacho-pdf'),
    url(r'^agregado/despacho/edit/(?P<pk>.*)/$', despacho.Edit_Despacho, name='edit-despacho'),
    url(r'^agregado/despacho/generar_pdf/(?P<pk>.*)/', despacho_pdf.factura_despacho_pdf, name='factura-despacho-pdf'),
   
    url(r'^agregado/total-despacho/add/$', despacho.Add_Total_Despacho, name='add-total-despacho'),

    url(r'^agregado/cuentasxcobrar/ver/$', despacho.Mostrar_CuetasXcobrar.as_view(), name='ver-cuentasx-cobrar'),
    url(r'^agregado/cuentasxcobrar/edit/(?P<pk>.*)/$', despacho.Editar_CuentasXcobrar, name='edit-cuentasx-cobrar'),

  
]
