CREATE TABLE Evaluaciones (
    EvaluacionID INT PRIMARY KEY IDENTITY(1,1), -- Clave primaria autoincremental
    Nombre VARCHAR(255) NOT NULL UNIQUE,       -- Nombre de la evaluación (añadido UNIQUE para evitar duplicados por nombre)
    Fecha DATE NOT NULL,                       -- Fecha de la evaluación
    Puntaje DECIMAL(5, 2) NOT NULL,            -- Puntaje de la evaluación (ej. 95.50)
    TipoEvaluacion VARCHAR(50) NOT NULL,       -- Para identificar el tipo (Examen, Trabajo, Presentacion)
    CONSTRAINT CK_Puntaje CHECK (Puntaje >= 0.00 AND Puntaje <= 100.00) -- Restricción para el puntaje
);

-- 2. Tabla para Exámenes
-- Almacena atributos específicos de los exámenes, con una clave foránea a Evaluaciones
CREATE TABLE Examenes (
    ExamenID INT PRIMARY KEY IDENTITY(1,1),
    EvaluacionID INT UNIQUE NOT NULL,          -- Clave foránea, debe ser única para cada evaluación
    Duracion INT NOT NULL,                     -- Duración del examen en minutos (Corregido a PascalCase)
    NumPreguntas INT NOT NULL,                 -- Número de preguntas (Corregido a PascalCase)
    CONSTRAINT FK_Examenes_Evaluaciones FOREIGN KEY (EvaluacionID)
        REFERENCES Evaluaciones(EvaluacionID)
        ON DELETE CASCADE,                      -- Si se borra la evaluación, se borra el examen
    CONSTRAINT CK_DuracionExamen CHECK (Duracion > 0),
    CONSTRAINT CK_NumPreguntas CHECK (NumPreguntas > 0)
);

-- 3. Tabla para Trabajos
-- Almacena atributos específicos de los trabajos, con una clave foránea a Evaluaciones
CREATE TABLE Trabajos (
    TrabajoID INT PRIMARY KEY IDENTITY(1,1),
    EvaluacionID INT UNIQUE NOT NULL,          -- Clave foránea, debe ser única para cada evaluación
    NumPaginas INT NOT NULL,                   -- Número de páginas del trabajo (Añadido y en PascalCase)
    Tema VARCHAR(500) NOT NULL,                -- Tema del trabajo (Añadido y en PascalCase)
    CONSTRAINT FK_Trabajos_Evaluaciones FOREIGN KEY (EvaluacionID)
        REFERENCES Evaluaciones(EvaluacionID)
        ON DELETE CASCADE,
    CONSTRAINT CK_NumPaginas CHECK (NumPaginas > 0)
);

-- 4. Tabla para Presentaciones
-- Almacena atributos específicos de las presentaciones, con una clave foránea a Evaluaciones
CREATE TABLE Presentaciones (
    PresentacionID INT PRIMARY KEY IDENTITY(1,1),
    EvaluacionID INT UNIQUE NOT NULL,          -- Clave foránea, debe ser única para cada evaluación
    Duracion INT NOT NULL,                     -- Duración de la presentación en minutos (Añadido y en PascalCase)
    TamanoAudiencia INT NOT NULL,              -- Tamaño de la audiencia (Añadido y en PascalCase)
    CONSTRAINT FK_Presentaciones_Evaluaciones FOREIGN KEY (EvaluacionID)
        REFERENCES Evaluaciones(EvaluacionID)
        ON DELETE CASCADE,
    CONSTRAINT CK_DuracionPresentacion CHECK (Duracion > 0),
    CONSTRAINT CK_TamanoAudiencia CHECK (TamanoAudiencia > 0)
);
GO