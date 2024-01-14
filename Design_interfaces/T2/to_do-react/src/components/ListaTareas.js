import React from 'react';
import ItemTareas from './ItemTareas';

const ListaTareas = ({ tareas, eliminarTarea, marcarComoCompletada }) => {
    return (
        <div>
            {tareas.map(tarea => (
                <ItemTareas
                    key={tarea.id}
                    tarea={tarea}
                    eliminarTarea={eliminarTarea}
                    marcarComoCompletada={marcarComoCompletada}
                />
            ))}
        </div>
    );
};

export default ListaTareas; 