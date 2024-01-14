import React, { useState } from 'react';

const AgregarTareas = ({ agregarTarea }) => {
  const [nuevaTarea, setNuevaTarea] = useState('');
  const [description, setDescription] = useState('');

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    if (name ==='nuevaTarea'){
      setNuevaTarea(value);
    }else if (name === 'description'){
      setDescription(value);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    agregarTarea(nuevaTarea, description);
    setNuevaTarea('');
    setDescription('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>Nueva Tarea
      <input 
        type="text"
        id="nuevaTarea"
        name="nuevaTarea"
        value={nuevaTarea}
        onChange={handleInputChange} />
      </label>
      <label>Descripción
      <input
        type="text"
        id="description"
        name="description"
        value={description}
        onChange={handleInputChange}/>
      </label>
      <button type="submit">Agregar Tarea</button>
    </form>
  );
};

export default AgregarTareas;
