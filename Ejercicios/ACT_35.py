mtrz= []
num_alum= []
nom_alum= []
tareasint= 0
listadetareas= []
tareasfinales= []
totaltareas= 0
porcentaje= []
promedio= []
reprobados= []
maxima= []
minima= []

from statistics import mean

calificaciones = open('calificaciones.csv', 'r')
sol = open('AnalysisResult.csv', 'w')
listalumnos = calificaciones.readlines(0)
sol.write('Id,Alumno,Calificación Final Tareas,Promedio calificaciones,Calificación Mayor,Calificación Menor,Alumnos Mayor Calificación,Alumnos Menor Calificación,Alumnos Reprobados\n')
for row in listalumnos:
    mtrz.append(row.split(','))
percentage= matrix[1][2::]
for i in range (len(percentage)-1):
    porcentaje.append(int(percentage[i][0:-1])/100)
porcentaje.append(int(percentage[-1][0:-2])/100)
for i in range (3, (len(matrix))):
    row = mtrz[i]
    num_alum.append(row[0])
    nom_alum.append(row[1])
    tarea = row[2::]
    for x in range (len(tareas)):
        totaltareas += int(tareas[x])
        tareasint += (int(tareas[x]) * porcentaje[x])
        listadetareas.append(int(tareas[x]))
    promedio.append(totaltareas/(len(porcentaje)))
    maxima.append(max(listadetareas))
    minima.append(min(listadetareas))
    tareasfinales.append(listadetareas)
    totaltareas = 0
    tareasint = 0
    listadetareas=[]
    if totaltareas[i-3]<60:
        reprobados.append('Reprobado')
    else:
        reprobados.append('')
for t in range (len(mtrz)-3):
    promedio_max = totaltareas.index(max(totaltareas))
    promedio_min = totaltareas.index(min(totaltareas))
    if t == promedio_max:
        sol.write(str(num_alum[t])+','+str(nom_alum[t])+','+str(tareasfinales[t])+','+str(promedio[t])+','+str(maxima[t])+','+str(minima[t])+',?,'+','+reprobados[t] +'\n')
    elif t == promedio_min:
        sol.write(str(num_alum[t])+','+str(nom_alum[t])+','+str(tareasfinales[t])+','+str(promedio[t])+','+str(maxima[t])+','+str(minima[t])+','+',?,'+reprobados[t] +'\n')
    else:
        sol.write(str(num_alum[t])+','+str(nom_alum[t])+','+str(tareasfinales[t])+','+str(promedio[t])+','+str(maxima[t])+','+str(minima[t])+','+','+reprobados[t] +'\n')
calificaciones.close()    
sol.close()    