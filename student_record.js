import React, { useState } from "react";


// Student Form Component

function StudentForm({ addStudent }) {

    const [name, setName] = useState("");

    const handleSubmit = (e) => {

        e.preventDefault();

        if (name.trim() === "") {
            return;
        }

        addStudent(name);

        setName("");
    };

    return (

        <div>

            <h2>Add Student</h2>

            <form onSubmit={handleSubmit}>

                <input
                    type="text"
                    placeholder="Enter student name"
                    value={name}
                    onChange={(e) =>
                        setName(e.target.value)
                    }
                />

                <button type="submit">
                    Add
                </button>

            </form>

        </div>
    );
}


// Student List Component

function StudentList({
    students,
    deleteStudent
}) {

    return (

        <div>

            <h2>Student List</h2>

            <ul>

                {students.map((student, index) => (

                    <li key={index}>

                        {student}

                        <button
                            onClick={() =>
                                deleteStudent(index)
                            }
                        >
                            Delete
                        </button>

                    </li>

                ))}

            </ul>

        </div>
    );
}


// Main App Component

function App() {

    const [students, setStudents] =
        useState([]);


    // Add Student

    const addStudent = (name) => {

        setStudents([
            ...students,
            name
        ]);
    };


    // Delete Student

    const deleteStudent = (index) => {

        const updatedStudents =
            students.filter(
                (_, i) => i !== index
            );

        setStudents(updatedStudents);
    };


    return (

        <div
            style={{
                padding: "20px",
                fontFamily: "Arial"
            }}
        >

            <h1>
                Student Record Management
            </h1>

            <StudentForm
                addStudent={addStudent}
            />

            <StudentList
                students={students}
                deleteStudent={deleteStudent}
            />

        </div>
    );
}

export default App;