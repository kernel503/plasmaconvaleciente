def getHospitales():
    hospitales = [
        ('Hospital Nacional "Arturo Morales" de Metapán','Hospital Nacional "Arturo Morales" de Metapán'),
        ('Hospital Nacional de Chalchuapa','Hospital Nacional de Chalchuapa'),
        ('Hospital Nacional de San Bartolo "Enfermera Angélica Vidal de Najarro"','Hospital Nacional de San Bartolo "Enfermera Angélica Vidal de Najarro"'),
        ('Hospital Nacional de Nueva Concepción','Hospital Nacional de Nueva Concepción'),
        ('Hospital Nacional de Ilobasco “Dr. José Luís Saca”','Hospital Nacional de Ilobasco “Dr. José Luís Saca”'),
        ('Hospital Nacional de Suchitoto','Hospital Nacional de Suchitoto'),
        ('Hospital Nacional de Ciudad Barrios “Monseñor Oscar Arnulfo Romero y Galdámez”','Hospital Nacional de Ciudad Barrios “Monseñor Oscar Arnulfo Romero y Galdámez”'),
        ('Hospital Nacional de Nueva Guadalupe','Hospital Nacional de Nueva Guadalupe'),    
        ('Hospital Nacional de Jiquilisco','Hospital Nacional de Jiquilisco'),   
        ('Hospital Nacional de Santiago de  María “Dr. Jorge Arturo Mena”','Hospital Nacional de Santiago de  María “Dr. Jorge Arturo Mena”'), 
        ('Hospital Nacional de Santa Rosa de Lima','Hospital Nacional de Santa Rosa de Lima'),
        ('Hospital Nacional de Ahuachapán “Francisco Menéndez”','Hospital Nacional de Ahuachapán “Francisco Menéndez”'),
        ('Hospital Nacional de Sonsonate “Dr. Jorge Mazzinni Villacorta”','Hospital Nacional de Sonsonate “Dr. Jorge Mazzinni Villacorta”'),
        ('Hospital Nacional Zacamil “Dr. Juan José Fernández”','Hospital Nacional Zacamil “Dr. Juan José Fernández”'),
        ('Hospital Nacional de Neumología y Medicina Familiar “Dr. José Antonio Saldaña”','Hospital Nacional de Neumología y Medicina Familiar “Dr. José Antonio Saldaña”'),
        ('Hospital Nacional de Soyapango “Dr. José Molina Martínez”','Hospital Nacional de Soyapango “Dr. José Molina Martínez”'),
        ('Hospital Nacional de Chalatenango “Dr. Luís Edmundo Vásquez”','Hospital Nacional de Chalatenango “Dr. Luís Edmundo Vásquez”'),
        ('Hospital Nacional San Rafael ','Hospital Nacional San Rafael '),
        ('Hospital Nacional de Zacatecoluca “SantaTeresa”','Hospital Nacional de Zacatecoluca “SantaTeresa”'),
        ('Hospital Nacional de Cojutepeque “Nuestra Sra. De Fátima”','Hospital Nacional de Cojutepeque “NuestraSra. De Fátima”'),
        ('Hospital Nacional de Sensuntepeque','Hospital Nacional de Sensuntepeque'),
        ('Hospital Nacional de San Vicente “SantaGertrudis”','Hospital Nacional de San Vicente “SantaGertrudis”'),
        ('Hospital Nacional de Usulután “San Pedro”','Hospital Nacional de Usulután “San Pedro”'),
        ('Hospital Nacional de Gotera “Dr. Héctor Antonio Hernández Flores”','Hospital Nacional de Gotera “Dr. Héctor Antonio Hernández Flores”'),
        ('Hospital Nacional de La Unión','Hospital Nacional de La Unión'),
        ('Hospital San Juan de Dios de Santa Ana','Hospital San Juan de Dios de Santa Ana'),
        ('Hospital San Juan de Dios de San Miguel','Hospital San Juan de Dios de San Miguel'),
        ('Hospital Nacional "Rosales"','Hospital Nacional "Rosales"'),
        ('Hospital Nacional de Niños "Benjamín Bloom"','Hospital Nacional de Niños "Benjamín Bloom"'),
        ('Hospital Nacional de Maternidad "Dr. Raúl Argüello Escolán"','Hospital Nacional de Maternidad "Dr. Raúl Argüello Escolán"'),
        ('Hospital Nacional Psiquiátrico "Dr. José Molina Martinez','Hospital Nacional Psiquiátrico "Dr. José Molina Martinez'),
        ('Hospital Nacional "Dr. Juan José Fernández"','Hospital Nacional "Dr. Juan José Fernández"'),
        ('Hospital Militar Central','Hospital Militar Central'),
        ]
    return hospitales

def buscar():
    print (getHospitales())
    hospitales = dict(getHospitales())
    print (hospitales)
    if 'Hospital El Salvadors' in hospitales:
        print ("se encuentra")
    else:
        print ("no se encuentras")

def getSangre():    
    tipoSangre=[
        ('A+','A RH+'),
        ('A-','A RH-'),
        ('B+','B RH+'),
        ('B-','B RH-'),
        ('AB+','AB RH+'),
        ('AB-','AB RH-'),
        ('O+','O RH+'),
        ('O-','O RH-'),
    ]
    return tipoSangre