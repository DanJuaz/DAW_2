import './App.css';
import ListaTareas from './components/ListaTareas';
import AgregarTareas from './components/AgregarTareas';
import { useState } from 'react';


function App() {
  const [tareas, setTareas] = useState([
    {id:0, title: 'Tarea De React', description: 'Crear un projecto de react, simulando el TO DO LIST', completed: false},
    {id:1, title: 'Tarea De Python', description: 'Crear un projecto de Python, simulando el TO DO LIST', completed: true},
    {id:2, title: 'Tarea De Vue', description: 'Crear un projecto de Vue, simulando el TO DO LIST', completed: false},
  ]);

  const agregarTarea = (nuevaTarea, description) => {
    const nuevaTareaObj = {
      id: tareas.length + 1,
      title: nuevaTarea,
      description: description,
      completed: false,
    };

    setTareas([...tareas, nuevaTareaObj]);
  };
  const eliminarTarea = (id) => {
    setTareas(tareas.filter(tarea => tarea.id !== id));
  };

  const marcarComoCompletada = (id) => {
    setTareas(tareas.map(tarea => (tarea.id === id ? { ...tarea, completed: !tarea.completed } : tarea)));
  };

  return (
    <div>
      <h1>Lista de Tareas</h1>
      <AgregarTareas agregarTarea={agregarTarea} />
      <ListaTareas
        tareas={tareas}
        eliminarTarea={eliminarTarea}
        marcarComoCompletada={marcarComoCompletada}
      />
    </div>
  );
};

export default App;
