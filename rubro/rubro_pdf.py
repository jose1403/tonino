from django.http import HttpResponse
from io import BytesIO
import os
import datetime
from django.contrib.auth.decorators import login_required
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
from .models import Rubro

raiz ='/agregado/productor/ver'

tiempo = datetime.datetime.now()

def logo_pdf():
    datos = DATOS_DE_LA_EMPRESA.objects.get(pk=1)
    url= '/home/chuy/proyectos/naturista/tonino/nucleo/static'
    string= '/media/%s'%str(datos.LOGO)
    fichero= os.path.normpath(os.path.join(os.path.dirname(__file__),'../nucleo/static/'))
    logo= Image('%s%s'%(fichero, datos.LOGO.url), width=300, height=100)
    logo.hAlign = 'LEFT'
    return logo


def rubro_pdf(request):
    print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "Listado-de-rubros.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    #response['Content-Disposition'] = 'attachment; filename=Listado_de_rubros-%s/%s/%s.pdf'%(tiempo.day,tiempo.month, tiempo.year)
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
    lista.append(logo_pdf())
    fecha= Paragraph('<b><i>Fecha: %s/%s/%s</i><b>'%(tiempo.day,tiempo.month, tiempo.year), styles['Normal'])
    lista.append(Spacer(0,15))
    lista.append(fecha)
    lista.append(Spacer(0,40))
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
   


    header = Paragraph("LISTADO DE RUBROS", styles['Heading1'])
    lista.append(header)
    headings = ('Codigo En Sistema', 'Nombre', 'Nombre Cientifico', 'T/Humedad', 'T/Impureza')
    array= []
    for p in Rubro.objects.all():
        array.append([Paragraph(p.codigo_en_sistema(), style_table),
                Paragraph(p.nombre, style_table), 
                Paragraph(p.nombre_cientifico, style_table),
                Paragraph('%s'%p.tolerancia_humedad, style_table),
                Paragraph('%s'%p.tolerancia_impureza, style_table)])

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
