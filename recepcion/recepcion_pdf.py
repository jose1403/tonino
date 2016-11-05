#-*- encoding: utf-8 -*-
from django.http import HttpResponse
from io import BytesIO
import os
import datetime
from django.contrib.auth.decorators import login_required, permission_required
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import Table
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.platypus import Image
from reportlab.platypus import Spacer
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0]
styles = getSampleStyleSheet()
from nucleo.models import DATOS_DE_LA_EMPRESA
from .models import Recepcion, PagoRecepcion, TotalRecepcion
from contabilidad.models import IMPUESTOS
raiz ='/agregado/productor/ver'

tiempo = datetime.datetime.now()


    
"""   a=0
       for i in lista:
           a += i.hectareas
           print a
       print b
       print lista
       print lista.count()"""
def logo_pdf():
    datos = DATOS_DE_LA_EMPRESA.objects.get(pk=1)
    url= '/home/chuy/proyectos/naturista/tonino/nucleo/static'
    string= '/media/%s'%str(datos.LOGO)
    fichero= os.path.normpath(os.path.join(os.path.dirname(__file__),'../nucleo/static/'))
    logo= Image('%s%s'%(fichero, datos.LOGO.url), width=200, height=100)
    logo.hAlign = 'LEFT'
    return logo

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def lista_recepcion_pdf(request, lista_pk, queryset):
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "Factura-Recepcion.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    #response['Content-Disposition'] = 'attachment; filename=%s-%s/%s/%s.pdf'%(pdf_name, tiempo.day,tiempo.month, tiempo.year)
    buff = BytesIO()
    datos= DATOS_DE_LA_EMPRESA.objects.get(pk=1)
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    cambio= False
    if type(lista_pk)== int:
        lista_pk= [lista_pk] 
        cambio=True
    model = queryset.filter(id__in=lista_pk)

    lista= []
    styles = getSampleStyleSheet()
    lista.append(logo_pdf())
    fecha= Paragraph('<b><i>Fecha: %s/%s/%s</i></b>'%(tiempo.day,tiempo.month, tiempo.year), styles['Normal'])
    lista.append(Spacer(0,40))
    lista.append(fecha)

    lista.append(Spacer(0,20))
    style= ParagraphStyle('Heading1')
    style.textColor= 'black'
    style.alignment= TA_CENTER
    style.fontSize= 18
    style.spaceAfter=15
    style.spaceBefore= 50
    style.spaceAfter=5
    style.leading = 20
    style.bulletIndent = 0
    style.allowOrphans = 0
    style.bulletFontSize = 10
    style.fontName='Helvetica'
    header = Paragraph("Listado de Recepciones".upper(), style)
    lista.append(header)
    lista.append(Spacer(0,10))

    #************Tabla****************************
    style_table= ParagraphStyle('Default')
    #style_table.textColor= 'black'
    style_table.alignment= TA_CENTER
    style_table.fontSize= 10
    style_table.spaceAfter=15
    style_table.spaceBefore= 0
    style_table.spaceAfter=0
    style_table.leading = 10 # anchor de tabla
    style_table.bulletIndent = 0
    style_table.allowOrphans = 0
    style_table.bulletFontSize = 5
    style_table.fontName='Times-Roman'
   
    style_table.bulletAnchor= 'start',
    cont= 0
    array=[]
    headings = ('CODIGO', 'PRODUCTO', 'CICLO', 'PROOVEDOR','CANTIDAD(H/I)', 'FECHA','TOTAL(Bs).')
    for p in model:
        pago = PagoRecepcion.objects.get(recepcion=p)
        total = TotalRecepcion.objects.get(ingreso=pago)
        cont+=1
        array.append([Paragraph(p.codigo_en_sistema(), style_table),
        Paragraph('%s (<font size=8>%s-%s</font>)'%(p.producto.nombre.upper(),p.variedad.nombre.upper(),p.tipo.nombre.upper()), style_table),
        Paragraph(p.ciclo_asociado.codigo_en_sistema(), style_table),
        Paragraph('%s'%p.proovedor.nombre_o_razon_social.upper(), style_table),
        Paragraph('%s Kg.'%total.cantidad_real, style_table),
        Paragraph('%s/%s/%s'%(p.fecha_agregado.day,p.fecha_agregado.month, p.fecha_agregado.year), style_table),
        Paragraph('%s'%(total.total_Bs), style_table)])

    t = Table([headings] + array)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (len(headings), -1), 2, colors.grey),
            ('LINEBELOW', (1, 0), (-1, 0), 2, colors.grey),
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor(0x41a02a)),
            ('BACKGROUND', (0, 1), (len(headings), len(array)), colors.HexColor(0xdbf706)),
            #('BACKGROUND', (0, 0), (-3, 0), colors.yellow),

            #('BACKGROUND', (0, 0), (-1, 0), colors.palegreen)d1e82af7

        ]
    ))
    lista.append(t)
    #recepcion= Recepcion.objects.get(pk=pk)
    
 
    


    doc.build(lista)
    response.write(buff.getvalue())
    buff.close()
    return response

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def factura_recepcion_pdf(request, pk):
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "Factura-Recepcion.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    #response['Content-Disposition'] = 'attachment; filename=%s-%s/%s/%s.pdf'%(pdf_name, tiempo.day,tiempo.month, tiempo.year)
    buff = BytesIO()
    datos= DATOS_DE_LA_EMPRESA.objects.get(pk=1)
    recepcion= Recepcion.objects.get(pk=pk)
    pago = PagoRecepcion.objects.get(recepcion=recepcion)
    total = TotalRecepcion.objects.get(ingreso=pago)

    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    styles = getSampleStyleSheet()
    lista= []
    stylefac= ParagraphStyle('Heading1')
    stylefac.textColor=('red')
    stylefac.alignment= TA_RIGHT
    stylefac.fontSize= 20
    stylefac.spaceBefore= 5
    stylefac.spaceAfter=5
    stylefac.leading = 10
    stylefac.bulletIndent = 0
    stylefac.allowOrphans = 0
    stylefac.bulletFontSize = 10
    
    stylefac.borderWidth = 0
    #stylemenbrete.bulletAnchor = start
    stylefac.borderPadding = 0
    stylefac.endDots = None
    lista.append(Paragraph('<font size=10 color=black><b>NO. Control</b></font>', stylefac))
    lista.append(Paragraph(recepcion.codigo_en_sistema(), stylefac))
    lista.append(logo_pdf())

    stylemenbrete= ParagraphStyle('Heading1')
    stylemenbrete.textColor=('black')
    stylemenbrete.alignment= TA_CENTER
    stylemenbrete.fontSize= 8
    stylemenbrete.spaceBefore= 5
    stylemenbrete.spaceAfter=5
    stylemenbrete.leading = 10
    stylemenbrete.bulletIndent = 0
    stylemenbrete.allowOrphans = 0
    stylemenbrete.bulletFontSize = 10
    
    stylemenbrete.borderWidth = 0
    #stylemenbrete.bulletAnchor = start
    stylemenbrete.borderPadding = 0
    stylemenbrete.endDots = None
    #stylemenbrete.textColor = Color(0,0,0,1)
    """MEMBRETE"""
    nombre= Paragraph(datos.NOMBRE.upper(), stylemenbrete)
    #fin **********************************
    rif = Paragraph('RIF: %s'% (datos.RIF.upper()), stylemenbrete)
    direccion=Paragraph('%s'% (datos.DIRECCION.upper()), stylemenbrete)
    telefonos =Paragraph('%s / %s'% (datos.TELEFONO, datos.CELULAR), stylemenbrete)
    codigo_postal=Paragraph('CODIGO POSTAL: %s'% (datos.CODIGO_POSTAL), stylemenbrete)
    lista.append(nombre)#+rif+direccion+telefonos+codigo_postal)
    lista.append(rif)#+rif+direccion+telefonos+codigo_postal)
    lista.append(direccion)
    lista.append(telefonos)
    lista.append(codigo_postal)
    lista.append(Spacer(0,30))
    #############################
    fecha= Paragraph('<b><i>Fecha de Emision: %s/%s/%s - %s:%s</i></b>'%(recepcion.fecha_agregado.day,recepcion.fecha_agregado.month, recepcion.fecha_agregado.year,recepcion.fecha_agregado.hour, recepcion.fecha_agregado.minute ), styles['Normal'])
    lista.append(fecha)
    lista.append(Spacer(0,10))
    lista.append(Paragraph('<para alignment=left><font><b>CICLO: %s </b></font>'%recepcion.ciclo_asociado, styles['Normal'])),


    lista.append(Paragraph('<font size=10 color=black ><b>-<b></font>'*156, styles['Normal']))
    lista.append(Paragraph('<font color=red><b>DATOS DEL PROOVEDOR</b><font> ', styles['Normal']))

    #datos De Proovedor
    style_table= ParagraphStyle('Default')
    #style_table.textColor= 'black'
    style_table.alignment= TA_CENTER
    style_table.fontSize= 10
    style_table.spaceAfter=15
    style_table.spaceBefore= 0
    style_table.spaceAfter=0
    style_table.leading = 10 # anchor de tabla
    style_table.bulletIndent = 0
    style_table.allowOrphans = 0
    style_table.bulletFontSize = 5
    style_table.fontName='Helvetica'

    style_table.bulletAnchor= 'start',
    array1=[]
    array1.append([Paragraph('<font color=black><b>NOMBRE O RAZON SOCIAL: %s</b>  </font>'%recepcion.proovedor.nombre_o_razon_social.upper(), style_table),
    Paragraph('<para alignment=left><font></b>CI/RIF: %s</b></font>'%recepcion.proovedor.documentoId.upper(), style_table)])
    array2=[]
    array2.append([Paragraph('<font><b>DOMICILIO: </b></font><font size=8></b>%s<b></font>'%recepcion.proovedor.domicilio_fiscal.upper(), style_table),
    Paragraph('<para alignment=left><font><b>TELE: %s/%s</b></font>'%(recepcion.proovedor.telefono, recepcion.proovedor.celular), style_table)])
    array3 =[]
    array3.append([Paragraph('<font><b>CODIGO: %s</b></font>'%recepcion.proovedor.codigo_en_sistema(), style_table),
    Paragraph('<font ><b>ZONA: %s</b></font>'%recepcion.zona_de_cosecha, style_table)])
    t=Table(array1 +array2 + array3)

    lista.append(t)
    lista.append(Paragraph('<font size=10 color=black ><b>-</b></font>'*156, styles['Normal']))

    descripcion= []
    
    headingsDes=[]
    headingsDes.append([Paragraph('<font color=black><b>RUBRO </b>  </font>', style_table),

        Paragraph('<para alignment=left><font><b>PRESIO </b></font>', style_table),

        Paragraph('<para alignment=left><font><b>CANTIDAD</b></font>', style_table),
        Paragraph('<para alignment=left><font><b>MERMA H/I</b></font>', style_table),
        Paragraph('<para alignment=left><font><b>CANTIDAD REAL</b></font>', style_table),

        Paragraph('<para alignment=left><font><b>TOTAL NETO. </b></font>', style_table),
        ])
    descripcion.append([Paragraph('<font color=black><b>%s<b>  </font>'%(recepcion.producto_total()),style_table),

    Paragraph('<para alignment=left><font><b> %s Bs.</b></font>'%pago.precio.precio_por_Kg, style_table),

    Paragraph('<para alignment=left><font><b> %s Kg.</b></font>'%recepcion.cantidad_en_Kg, style_table),
    Paragraph('<para alignment=left><font><b> %s %%</b></font>'%total.descuentoTotal, style_table),

    Paragraph('<para alignment=left><font><b> %s Kg.</b></font>'%total.cantidad_real, style_table),


    Paragraph('<para alignment=left><font><b> %s Bs.</b></font>'%total.total_neto, style_table),
    ])
    separator=('', '','', '')
    #headingsDes=('Rubro', 'precio','Cantidad Recibida', 'Total Neto')
    imptable=[]
    impuesto1=[]
    print total.impuestos()
    for i, k in total.impuestos().items():
        impuesto1.append([Paragraph('<font color=black><b> </b>  </font>', style_table),
        Paragraph('<para alignment=left><font><b> </b></font>', style_table),
        Paragraph('<para alignment=left><font><b> </b></font>', style_table),
        Paragraph('<para alignment=left><font><b> </b></font>', style_table),

        

        Paragraph('<para alignment=left><font><b>%s </b></font>'%i, style_table),
        Paragraph('<para alignment=left><font><b>%s Bs.</b></font>'%k, style_table),
        ])
    precio_total=[]
    precio_total.append([Paragraph('<font color=black><b> </b>  </font>', style_table),
        Paragraph('<para alignment=left><font><b> </b></font>', style_table),
        Paragraph('<para alignment=left><font><b> </b></font>', style_table),
        Paragraph('<para alignment=left><font><b> </b></font>', style_table),
        
        Paragraph('<para alignment=left><font><b>TOTAL </b></font>', style_table),
        Paragraph('<para alignment=left><font><b>%s Bs. </b></font>'%total.total_Bs, style_table),
        ])
    tdescripcion= Table(headingsDes+ descripcion+[separator]+impuesto1+precio_total)
    lista.append( tdescripcion)
    lista.append(Spacer(0, 40))
    style_analisis= ParagraphStyle('Default')
    #style_table.textColor= 'black'
    #style_table.alignment= TA_CENTER
    style_analisis.fontSize= 10
    style_analisis.spaceAfter=15
    style_analisis.spaceBefore= 0
    style_analisis.spaceAfter=0
    style_analisis.leading = 20 # anchor de tabla
    style_analisis.bulletIndent = 0
    style_analisis.allowOrphans = 0
    style_analisis.bulletFontSize = 5
    style_analisis.fontName='Times-Roman'
    lista.append(Paragraph('<para alignment=left><font size=10><b> DESCUENTO POR IMPURESA: %s%%</b> </font>'% total.descuentoI, style_analisis))
    lista.append(Paragraph('<para alignment=left><font size=10><b>MERMA POR HUMEDAD:%s%% </b> </font>'%total.descuentoH, style_analisis))
    lista.append(Paragraph('<para alignment=left><font size=10><b>DESCUENTO POR MANIPULEO: %s%%</b> <i> </i> </font>'%total.descuentoM, style_analisis))

    lista.append(Paragraph('<para alignment=left><font size=12 color=grey><b>RESULTADOS DEL ANALISIS</b></font>', style_analisis))
    lista.append(Paragraph('<para alignment=left><font size=10><b> HUMEDAD:%s%%</b></font>'% recepcion.humedad, style_analisis))
    lista.append(Paragraph('<para alignment=left><font size=10><b>GRANOS DAÑADOS: %s%%</b></font>'%recepcion.granos_danados_totales, style_analisis))
    lista.append(Paragraph('<para alignment=left><font size=10><b>GRANOS PARTIDOS: %s%%</b> </font>'%recepcion.granos_partidos, style_analisis))
    lista.append(Paragraph('<para alignment=left><font size=10><b>TEMPERATURA PROMEDIO: %s°C</b></font>'%recepcion.temperatura_promedio, style_analisis))
    lista.append(Paragraph('<para alignment=left><font size=10><b>OTROS:</b> <i>%s%% </i> </font>'%recepcion.otros, style_analisis))

    doc.build(lista)
    response.write(buff.getvalue())
    buff.close()
    return response
