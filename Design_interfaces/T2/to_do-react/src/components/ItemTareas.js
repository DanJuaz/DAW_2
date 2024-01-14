import React from "react";

const ItemTareas = ({ tarea, eliminarTarea, marcarComoCompletada }) => {
  const { id, title, description, completed } = tarea;

  return (
    <div
      style={{
        border: "1px solid #ccc",
        padding: "10px",
        marginBottom: "10px",
      }}
    >
      <h3>{title}</h3>
      <p>{description}</p>
      <p>{completed ? "Completada" : "Pendiente"}</p>
      <button onClick={() => marcarComoCompletada(id)}>
        {completed ? "Marcar como Pendiente" : "Marcar como Completada"}
      </button>

      <button onClick={() => eliminarTarea(id)}>Eliminar Tarea</button>
    </div>
  );
};

export default ItemTareas;
