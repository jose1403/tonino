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
from .models import Cliente

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
    logo= Image('%s%s'%(fichero, datos.LOGO.url), width=300, height=100)
    logo.hAlign = 'LEFT'
    return logo


@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def lista_clientes_pdf(request):
    print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "Listado-de-Proovedores.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    #response['Content-Disposition'] = 'attachment; filename=%s-%s/%s/%s.pdf'%(pdf_name, tiempo.day,tiempo.month, tiempo.year)
    buff = BytesIO()

    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    styles = getSampleStyleSheet()
    lista = []
    lista.append(logo_pdf())
    fecha= Paragraph('<b><i>Fecha: %s/%s/%s</i></b>'%(tiempo.day,tiempo.month, tiempo.year), styles['Normal'])
    
    lista.append(Spacer(0,40))
    lista.append(fecha)

    lista.append(Spacer(0,10))
    style= ParagraphStyle('Heading1')
    style.textColor= 'black'
    style.alignment= TA_CENTER
    style.fontSize= 18
    style.spaceAfter=15
    style.spaceBefore= 30
    style.spaceAfter=5
    style.leading = 20
    style.bulletIndent = 0
    style.allowOrphans = 0
    style.bulletFontSize = 10
    style.fontName='Helvetica'
    header = Paragraph("<b>Listado de Clientes</b>".upper(), style)
    lista.append(header)
    lista.append(Spacer(0,10))

    #************Tabla****************************
    style_table= ParagraphStyle('Default')
    #style_table.textColor= 'black'
    #style_table.alignment= TA_CENTER
    style_table.fontSize= 10
    style_table.spaceAfter=15
    style_table.spaceBefore= 0
    style_table.spaceAfter=0
    style_table.leading = 20 # anchor de tabla
    style_table.bulletIndent = 0
    style_table.allowOrphans = 0
    style_table.bulletFontSize = 5
    style_table.fontName='Times-Roman'
   
    style_table.bulletAnchor= 'start',
    cont= 0
    array=[]
    headings = ('N','CODIGO', 'NOMBRE', 'CI/RIF', 'DOMICILIO FISCAL','TELEFONO', 'CELULAR')
    for p in Cliente.objects.filter(habilitado=True).order_by('fecha_agregado'):
        cont+=1
        array.append([Paragraph(str(cont), style_table),
        Paragraph(p.codigo_en_sistema(), style_table),
        Paragraph(p.nombre_o_razon_social.title(), style_table),
        Paragraph(p.documentoId.title(), style_table),
        Paragraph(p.domicilio_fiscal.title(), style_table),
        Paragraph(p.telefono, style_table),
        Paragraph(p.celular, style_table)])

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
    doc.build(lista)
    response.write(buff.getvalue())
    buff.close()
    return response


@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def info_cliente_pdf(request, pk):
   
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "info-de-cliente.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    print inch
    #response['Content-Disposition'] = 'attachment; filename=%s-%s/%s/%s.pdf'%(pdf_name, tiempo.day,tiempo.month, tiempo.year)
    #response['Content-Disposition'] = 'filename="archivo.pdf"' 

    buff = BytesIO()


    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )

    lista = []
    styles = getSampleStyleSheet()
    #menbrete ************************
    lista.append(logo_pdf())
    fecha= Paragraph('<b><i>Fecha: %s/%s/%s</i></b>'%(tiempo.day,tiempo.month, tiempo.year), styles['Normal'])
    lista.append(Spacer(0,25))
    
    lista.append(fecha)
    lista.append(Spacer(0,20))
    style= ParagraphStyle('Heading1')
    style.textColor= 'black'
    style.alignment= TA_CENTER
    style.fontSize= 16
    style.spaceAfter=15
    style.spaceBefore= 30
    style.spaceAfter=5
    style.leading = 20
    style.bulletIndent = 0
    style.allowOrphans = 0
    style.bulletFontSize = 10
    fecha = Paragraph

    style_C= ParagraphStyle('Normal')
    style_C.alignment= TA_RIGHT
    style_C.fontSize= 14
    style_C.textColor= 'black'


    style_N= ParagraphStyle('Normal')
    style_N.alignment= TA_LEFT
    style_N.fontSize= 12
    style_N.textColor= 'black'
    header = Paragraph("<b>Informacion de Cliente</b>".upper(), style)

    #******Modelos********
    lista.append(header)
    lista.append(Spacer(0,25))


    #******Modelos********
    p=  Cliente.objects.get(pk=pk, habilitado=True)

    #******Modelos********
   
    #
    style_C= ParagraphStyle('Normal')
    style_C.alignment= TA_RIGHT
    style_C.fontSize= 14
    style_C.textColor= 'black'

    lista.append(Paragraph('<font ><b>CODIGO EN SISTEMA:</b> %s</font>'%p.codigo_en_sistema(),style_C))

    style_N= ParagraphStyle('Normal')
    style_N.alignment= TA_LEFT
    style_N.fontSize= 12
    style_N.textColor= 'black'

    style_table= ParagraphStyle('Default')
    #style_table.textColor= 'black'
    #style_table.alignment= TA_CENTER
    style_table.fontSize= 10
    style_table.spaceAfter=15
    style_table.spaceBefore= 0
    style_table.spaceAfter=0
    style_table.leading = 20 # anchor de tabla
    style_table.bulletIndent = 0
    style_table.allowOrphans = 0
    style_table.bulletFontSize = 5
    style_table.fontName='Times-Roman'
   
    style_table.bulletAnchor= 'start',
    lista.append(Paragraph('<font><b>INFORMACION BASICA</b></font>', style_N))
    lista.append(Spacer(0, 20))
    array_datos=[]
    title_datos= ('Nombre o Razon Social', 'CI/RIF', 'Domicilio Fiscal')
    array_datos.append([
    Paragraph(p.nombre_o_razon_social.title(), style_table),
    Paragraph(p.documentoId.title(), style_table),
    Paragraph(p.domicilio_fiscal.title(), style_table)])
    t_datos=Table([title_datos]+ array_datos)
    tupla_tabla=  [
            ('GRID', (0, 1), (len(title_datos), -1), 1, colors.black),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),

            ('LINEBELOW', (1, 0), (-1, 0), 1, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('BACKGROUND', (0, 1), (len(title_datos), len(array_datos)), colors.white)#HexColor(0x979494)),
            #('BACKGROUND', (0, 0), (-3, 0), colors.yellow),

            #('BACKGROUND', (0, 0), (-1, 0), colors.palegreen)d1e82af7

        ]
    t_datos.setStyle(TableStyle(tupla_tabla))#414141
    lista.append(t_datos)
    array_referencia=[]
    title_referencia= ('TELEFONO', 'CELULAR', 'E-MAIL')
    array_referencia.append([
    Paragraph(p.telefono, style_table),
    Paragraph(p.celular, style_table),
    Paragraph(p.e_mail, style_table)])
    t_referencia=Table([title_referencia]+ array_referencia)
    t_referencia.setStyle(TableStyle(tupla_tabla))
    lista.append(t_referencia)

    array_banco= []
    encabesado_banco=('', 'CUENTA PRINCIPAL', '')
    title_banco= ('CUENTA','BANCO', 'TIPO')
    array_banco.append([ Paragraph(p.cuenta_bancaria, style_table),
    Paragraph(p.banco.nombre.title(), style_table),
    Paragraph(p.tipo_cuenta.nombre.title(), style_table),
   ])
    t_banco=Table([title_banco]+ array_banco)
    t_banco.setStyle(TableStyle(tupla_tabla))
    lista.append(t_banco)

    array_afiliacion=[]
    title_afiliacion= ('FECHA DE AGREGADO', 'REFENCIA', 'OBSERVACION')
    array_afiliacion.append([
    Paragraph('%s/%s/%s'%(p.fecha_agregado.day, p.fecha_agregado.month,p.fecha_agregado.year), style_table),
    Paragraph(p.referencia_folder, style_table),
    Paragraph(p.observacion, style_table)])
    t_afiliacion=Table([title_afiliacion]+ array_afiliacion)
    t_afiliacion.setStyle(TableStyle(tupla_tabla))
    lista.append(t_afiliacion)
 

    
   





    doc.build(lista)#, onFirstPage = myFirstPage, onLaterPages = myLaterPages)#doc.build(story, onFirstPage = myFirstPage, onLaterPages = myLaterPages)

    response.write(buff.getvalue())
    buff.close()
    return response

def info_productor_pdf(request, pk):
   
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "info-de-Productor.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    print inch
    #response['Content-Disposition'] = 'attachment; filename=%s-%s/%s/%s.pdf'%(pdf_name, tiempo.day,tiempo.month, tiempo.year)
    #response['Content-Disposition'] = 'filename="archivo.pdf"' 

    buff = BytesIO()


    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            showBoundary=0,
                            title='Info-Productores',
                            onPage='doNothing',
                            onPageEnd='doNothing'
                            )

    lista = []
    styles = getSampleStyleSheet()
    #menbrete ************************
    lista.append(logo_pdf())
    fecha= Paragraph('<b><i>Fecha: %s/%s/%s</i></b>'%(tiempo.day,tiempo.month, tiempo.year), styles['Normal'])
    lista.append(Spacer(0,25))
    lista.append(fecha)
    lista.append(Spacer(0,20))
    style= ParagraphStyle('Heading1')
    style.textColor= 'black'
    style.alignment= TA_CENTER
    style.fontSize= 16
    style.spaceAfter=15
    style.spaceBefore= 15
    style.spaceAfter=5
    style.leading = 20
    style.bulletIndent = 0
    style.allowOrphans = 0
    style.bulletFontSize = 10
    header = Paragraph("<b>Informacion del Proovedor</b>".upper(), style)

    #******Modelos********
    lista.append(header)
    lista.append(Spacer(0,25))

    p=  Productor.objects.get(pk=pk, habilitado=True, null=False)
    zona = Productor.zona.contar_zonas(pk=pk, null=False)

    #******Modelos********
   
    #
    style_C= ParagraphStyle('Normal')
    style_C.alignment= TA_RIGHT
    style_C.fontSize= 14
    style_C.textColor= 'black'


    style_N= ParagraphStyle('Normal')
    style_N.alignment= TA_LEFT
    style_N.fontSize= 12
    style_N.textColor= 'black'

    style_table= ParagraphStyle('Default')
    #style_table.textColor= 'black'
    #style_table.alignment= TA_CENTER
    style_table.fontSize= 10
    style_table.spaceAfter=15
    style_table.spaceBefore= 0
    style_table.spaceAfter=0
    style_table.leading = 20 # anchor de tabla
    style_table.bulletIndent = 0
    style_table.allowOrphans = 0
    style_table.bulletFontSize = 5
    style_table.fontName='Times-Roman'
   
    style_table.bulletAnchor= 'start',
    codigo_en_sistema = Paragraph('<font ><b>CODIGO EN SISTEMA:</b> %s</font>'%p.codigo_en_sistema(),style_C)
    lista.append(codigo_en_sistema)
    lista.append(Spacer(0, 5))
    lista.append(Paragraph('<b>NUMERO DE ZONAS:</b>%s'%zona['CantZonas'], style_N))
    lista.append(Spacer(0, 10))

    lista.append(Paragraph('<b> CANTIDAD DE HECTAREAS:</b> %s Hect.'%zona['CantHectareas'], style_N))
    lista.append(Spacer(0, 20))
    array_datos=[]

    lista.append(Paragraph('<font><b>INFORMACION BASICA</b></font>', style_N))
    lista.append(Spacer(0, 20))

    title_datos= ('Nombre o Razon Social', 'CI/RIF', 'Domicilio Fiscal')
    array_datos.append([
    Paragraph(p.nombre_o_razon_social.title(), style_table),
    Paragraph(p.documentoId.title(), style_table),
    Paragraph(p.domicilio_fiscal.title(), style_table)])
    t_datos=Table([title_datos]+ array_datos)
    tupla_tabla=  [
            ('GRID', (0, 1), (len(title_datos), -1), 1, colors.black),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),

            ('LINEBELOW', (1, 0), (-1, 0), 1, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('BACKGROUND', (0, 1), (len(title_datos), len(array_datos)), colors.white)#HexColor(0x979494)),
            #('BACKGROUND', (0, 0), (-3, 0), colors.yellow),

            #('BACKGROUND', (0, 0), (-1, 0), colors.palegreen)d1e82af7

        ]
    t_datos.setStyle(TableStyle(tupla_tabla))#414141
    lista.append(t_datos)
    array_referencia=[]
    title_referencia= ('TELEFONO', 'CELULAR', 'E-MAIL')
    array_referencia.append([
    Paragraph(p.telefono, style_table),
    Paragraph(p.celular, style_table),
    Paragraph(p.e_mail, style_table)])
    t_referencia=Table([title_referencia]+ array_referencia)
    t_referencia.setStyle(TableStyle(tupla_tabla))
    lista.append(t_referencia)

    array_banco= []
    encabesado_banco=('', 'CUENTA PRINCIPAL', '')
    title_banco= ('CUENTA','BANCO', 'TIPO')
    array_banco.append([ Paragraph(p.cuenta_bancaria, style_table),
    Paragraph(p.banco.nombre.title(), style_table),
    Paragraph(p.tipo_cuenta.nombre.title(), style_table),
   ])
    t_banco=Table([title_banco]+ array_banco)
    t_banco.setStyle(TableStyle(tupla_tabla))
    lista.append(t_banco)

    array_afiliacion=[]
    title_afiliacion= ('FECHA DE AGREGADO', 'REFENCIA', 'OBSERVACION')
    array_afiliacion.append([
    Paragraph('%s/%s/%s'%(p.fecha_agregado.day, p.fecha_agregado.month,p.fecha_agregado.year), style_table),
    Paragraph(p.referencia_folder, style_table),
    Paragraph(p.observacion, style_table)])
    t_afiliacion=Table([title_afiliacion]+ array_afiliacion)
    t_afiliacion.setStyle(TableStyle(tupla_tabla))
    lista.append(t_afiliacion)
 

    
   





    doc.build(lista)#, onFirstPage = myFirstPage, onLaterPages = myLaterPages)#doc.build(story, onFirstPage = myFirstPage, onLaterPages = myLaterPages)

    response.write(buff.getvalue())
    buff.close()
    return response
#*********************************************************



Title = "Hello world"
pageinfo = "platypus example"

from reportlab.pdfgen import canvas
@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def convertir_pdf(request):
    import os
    try: 
        libro = DATOS_DE_LA_EMPRESA.objects.get(pk=1) 
    except ValueError: 
        raise Http404() 
    response = HttpResponse(content_type='application/pdf') 

    buffer = BytesIO() 
    p = canvas.Canvas(buffer)
    from reportlab.lib.units import inch
    p.translate(PAGE_WIDTH/6.0, PAGE_HEIGHT-150)
    p.setFont("Helvetica", 14)
    p.setStrokeColorRGB(0.2,0.5,0.3)
    p.setFillColorRGB(1,0,1)
    p.line(0,0,0,1.7*inch)
    p.line(0,0,1*inch,0)
    p.rect(0.2*inch,0.2*inch,1*inch,1.5*inch, fill=1)
    p.rotate(0)
    p.setFillColorRGB(1,1,1)
    fichero= os.path.normpath(os.path.join(os.path.dirname(__file__),'../nucleo/static'))
    fichero_logo= '%s/indice.jpeg'% fichero
    p.drawImage('%s%s'%(fichero, libro.LOGO.url), 0.3*inch, -inch, width=250, height=100)#drawString(0.3*inch, -inch, "Hello World")

    p.roundRect(0, 750, 694, 120, 20, stroke=0, fill=1)
    p.setFillColorRGB(1,1,1) 
    p.drawString(100, 800, str(libro.NOMBRE))
    #p.drawImage(str(libro.LOGO.url), 100, 100, width=400, height=600)
    fichero= os.path.normpath(os.path.join(os.path.dirname(__file__),'../nucleo/static'))
    fichero_logo= '%s/indice.jpeg'% fichero
    p.drawImage('%s%s'%(fichero, libro.LOGO.url), 300, 600, width=250, height=100)
    p.showPage() 
    p.save() 
    pdf = buffer.getvalue() 
   
    buffer.close() 
    response.write(pdf) 
    return response






def myFirstPage(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Bold',16)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "First Page / %s" % pageinfo)
    canvas.restoreState()

def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "Page %d %s" % (doc.page, pageinfo))
    canvas.restoreState()

def go(request):
    """print 'inicio'
                response = HttpResponse(content_type='application/pdf')
                #pdf_name = "info-de-Productor.pdf"
                #response['Content-Disposition'] = 'attachment; filename=%s-%s/%s/%s.pdf'%(pdf_name, tiempo.day,tiempo.month, tiempo.year)
                buff = BytesIO()
                doc = SimpleDocTemplate(buff,
                                        pagesize=letter,
                                        rightMargin=40,
                                        leftMargin=40,
                                        topMargin=60,
                                        bottomMargin=18,)
            
                Story = [Spacer(1,1*inch)]
                style = styles["Normal"]
                for i in range(100):
                    bogustext = ("This is Paragraph number %s. " % i) *20
                    p = Paragraph(bogustext, styles['Normal'])
                    Story.append(p)
                    Story.append(Spacer(1,0.2*inch))
                doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)
                response.write(buff.getvalue())
                buff.close()
                return response"""



def titulo_pdf_proovedor(canvas, doc):
    datos = DATOS_DE_LA_EMPRESA.objects.get(pk=1)
    membrete= '%s \n RIF %s \n DIRECCION: %s \n TELEFONOS: %s / %s \n ZONA POSTAL: %s'%(datos.NOMBRE.upper(),
                                     datos.RIF.upper(), datos.DIRECCION.upper(),
                                     datos.TELEFONO, datos.CELULAR,
                                     datos.CODIGO_POSTAL)
    nombre= datos.NOMBRE.upper()
    rif = 'RIF: %s'% (datos.RIF.upper())
    direccion= 'DIRECCION: %s'% (datos.DIRECCION.upper())
    telefonos = '%s / %s'% (datos.TELEFONO, datos.CELULAR)
    codigo_postal='CODIGO POSTAL: %s'% (datos.CODIGO_POSTAL)


    canvas.saveState()
    canvas.setFillColorRGB(0,0,0)
    #canvas.drawCentredString(50, PAGE_HEIGHT-150, membrete)

    #canvas.drawString(100, 800, str(libro.titulo))#Obtenemos el titulo de un libro y lap.drawImage(str(libro.portada.url), 100, 100, width=400, height=600) 
    # mostramos y guardamos el objeto PDF. 

    canvas.setFont('Times-Bold',12)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-110, nombre)
    canvas.roundRect(0, 750, 694, 120, 20, stroke=0, fill=1) 

    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-130, rif)
    textobject = canvas.beginText()
    textobject.setTextOrigin(inch, 400)
    textobject.setFont("Helvetica-Oblique", 14)
    for line in direccion:
        textobject.textLine(line)
    textobject.setFillGray(0.4)
    textobject.textLines(direccion)
    canvas.drawText(textobject)
    #canvas.drawString(100, 100, direccion)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-170, telefonos)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-190, codigo_postal)

    canvas.drawString(12, 10 * 50, "First Page / %s" % membrete)

    canvas.restoreState()

def formato_menbrete_pdf():
    lista= []
    stylemenbrete= ParagraphStyle('Heading1')
    stylemenbrete.textColor=('black')
    stylemenbrete.alignment= TA_CENTER
    stylemenbrete.fontSize= 12
    stylemenbrete.spaceBefore= 5
    stylemenbrete.spaceAfter=5
    stylemenbrete.leading = 20
    stylemenbrete.bulletIndent = 0
    stylemenbrete.allowOrphans = 0
    stylemenbrete.bulletFontSize = 10
    
    stylemenbrete.borderWidth = 0
    #stylemenbrete.bulletAnchor = start
    stylemenbrete.borderPadding = 0
    stylemenbrete.endDots = None
    #stylemenbrete.textColor = Color(0,0,0,1)
    nombre= Paragraph(datos.NOMBRE.upper(), stylemenbrete)
    #fin **********************************
    rif = Paragraph('RIF: %s'% (datos.RIF.upper()), stylemenbrete)
    direccion=Paragraph('DIRECCION: %s'% (datos.DIRECCION.upper()), stylemenbrete)
    telefonos =Paragraph('%s / %s'% (datos.TELEFONO, datos.CELULAR), stylemenbrete)
    codigo_postal=Paragraph('CODIGO POSTAL: %s'% (datos.CODIGO_POSTAL), stylemenbrete)
    lista.append(nombre)#+rif+direccion+telefonos+codigo_postal)
    lista.append(rif)#+rif+direccion+telefonos+codigo_postal)
    lista.append(direccion)
    lista.append(telefonos)
    lista.append(codigo_postal)
