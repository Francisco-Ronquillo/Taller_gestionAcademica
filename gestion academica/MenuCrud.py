import os
import time
from Utilidades import Utilidades,gotoxy,limpiarPantalla
from CrudEstudiante import menuEstudiante
from CrudProfesor import menuProfesor
from CrudNivel import menuNivel
from CrudPeriodo import menuPeriodo
from CrudAsignatura import menuAsignatura
from CrudNotas import menuNota
from CrudTesis import menuTesis
option=''
while option!='5':
   limpiarPantalla()
   menuMain=Utilidades('Menu Academico',['Estudiante','Profesor','Periodo','Asignatura','Nivel','Notas','Tesis','Salir'])
   option=menuMain.menu()
   if option=='1':
      option=''
      while option!='5':
         limpiarPantalla()
         menuEstudiantes=Utilidades('Menu Estudiante',['Registrar','Actualizar','Eliminar','Consultar','Salir'])
         option=menuEstudiantes.menu()
         if option=='1':
            menuEstudiante.create()
         if option=='2':
            menuEstudiante.update()
         if option=='3':
            menuEstudiante.delete()
         if option=='4':
            menuEstudiante.consult()
         if option=='5':
            limpiarPantalla()
            print('Volviendo al menu principal')
            time.sleep(2)
      option=''
   if option=='2':
      option=''
      while option!='5':
         limpiarPantalla()
         menuProfesors=Utilidades('Menu Profesor',['Registrar','Actualizar','Eliminar','Consultar','Salir'])
         option=menuProfesors.menu()
         if option=='1':
            menuProfesor.create()
         if option=='2':
            menuProfesor.update()
         if option=='3':
            menuProfesor.delete()
         if option=='4':
            menuProfesor.consult()
         if option=='5':
            limpiarPantalla()
            print('Volviendo al menu principal')
            time.sleep(2)
      option=''
   if option=='3':
      option=''
      while option!='5':
         limpiarPantalla()
         menuPeriodos=Utilidades('Menu Periodo',['Registrar','Actuazilar','Eliminar','Consultar','Salir'])
         option=menuPeriodos.menu()
         if option=='1':
            menuPeriodo.create()
         if option=='2':
            menuPeriodo.update()
         if option=='3':
            menuPeriodo.delete()
         if option=='4':
            menuPeriodo.consult()
         if option=='5':
            limpiarPantalla()
            print('Volviendo al menu principal')
            time.sleep(2)
      option=''
   if option=='4':
      option=''
      while option!='5':
         limpiarPantalla()
         menuAsignaturas=Utilidades('Menu Asignatura',['Registrar','Actualizar','Eliminar','Consultar','Salir'])
         option=menuAsignaturas.menu()
         if option=='1':
            menuAsignatura.create()
         if option=='2':
            menuAsignatura.update()
         if option=='3':
            menuAsignatura.delete()
         if option=='4':
            menuAsignatura.consult()
         if option=='5':
            limpiarPantalla()
            print('Volviendo al menu principal')
            time.sleep(2)
      option=''
   if option=='5':
         option=''
         while option!='5':
            limpiarPantalla()
            menuNivels=Utilidades('Menu Nivel',['Registrar','Actualizar','Eliminar','Consultar','Salir'])
            option=menuNivels.menu()
            if option=='1':
               menuNivel.create()
            if option=='2':
               menuNivel.update()
            if option=='3':
               menuNivel.delete()
            if option=='4':
               menuNivel.consult()
            if option=='5':
               limpiarPantalla()
               print('Volviendo al menu principal')
               time.sleep(2)
         option=''
   if option=='6':
         option=''
         while option!='5':
            limpiarPantalla()
            menuNotas=Utilidades('Menu Nota',['Registrar','Actualizar','Eliminar','Consultar','Salir'])
            option=menuNotas.menu()
            if option=='1':
               menuNota.create()
            if option=='2':
               menuNota.update()
            if option=='3':
               menuNota.delete()
            if option=='4':
               menuNota.consult()
            if option=='5':
               limpiarPantalla()
               print('Volviendo al menu principal')
               time.sleep(2)
         option=''
   if option=='7':
      option=''
      while option!='7':
            limpiarPantalla()
            menuTesi=Utilidades('Menu Tesis',['Registrar','Actualizar','Eliminar','Consultar','Salir'])
            option=menuTesi.menu()
            if option=='1':
                  menuTesis.create()
            if option=='2':
                  menuTesis.update()
            if option=='3':
               menuTesis.delete()
            if option=='4':
               menuTesis.consult()
            if option=='5':
               limpiarPantalla()
               print('Volviendo al menu principal')
               time.sleep(2)
   if option=='8':
      limpiarPantalla()
      print('Saliendo del programa')
      time.sleep(2)
      break

