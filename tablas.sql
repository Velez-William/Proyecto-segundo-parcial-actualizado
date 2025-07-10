CREATE TABLE Evaluaciones (
    EvaluacionID INT PRIMARY KEY IDENTITY(1,1), -- Clave primaria autoincremental
    Nombre VARCHAR(255) NOT NULL UNIQUE,       -- Nombre de la evaluaci�n (a�adido UNIQUE para evitar duplicados por nombre)
    Fecha DATE NOT NULL,                       -- Fecha de la evaluaci�n
    Puntaje DECIMAL(5, 2) NOT NULL,            -- Puntaje de la evaluaci�n (ej. 95.50)
    TipoEvaluacion VARCHAR(50) NOT NULL,       -- Para identificar el tipo (Examen, Trabajo, Presentacion)
    CONSTRAINT CK_Puntaje CHECK (Puntaje >= 0.00 AND Puntaje <= 100.00) -- Restricci�n para el puntaje
);

-- 2. Tabla para Ex�menes
-- Almacena atributos espec�ficos de los ex�menes, con una clave for�nea a Evaluaciones
CREATE TABLE Examenes (
    ExamenID INT PRIMARY KEY IDENTITY(1,1),
    EvaluacionID INT UNIQUE NOT NULL,          -- Clave for�nea, debe ser �nica para cada evaluaci�n
    Duracion INT NOT NULL,                     -- Duraci�n del examen en minutos (Corregido a PascalCase)
    NumPreguntas INT NOT NULL,                 -- N�mero de preguntas (Corregido a PascalCase)
    CONSTRAINT FK_Examenes_Evaluaciones FOREIGN KEY (EvaluacionID)
        REFERENCES Evaluaciones(EvaluacionID)
        ON DELETE CASCADE,                      -- Si se borra la evaluaci�n, se borra el examen
    CONSTRAINT CK_DuracionExamen CHECK (Duracion > 0),
    CONSTRAINT CK_NumPreguntas CHECK (NumPreguntas > 0)
);

-- 3. Tabla para Trabajos
-- Almacena atributos espec�ficos de los trabajos, con una clave for�nea a Evaluaciones
CREATE TABLE Trabajos (
    TrabajoID INT PRIMARY KEY IDENTITY(1,1),
    EvaluacionID INT UNIQUE NOT NULL,          -- Clave for�nea, debe ser �nica para cada evaluaci�n
    NumPaginas INT NOT NULL,                   -- N�mero de p�ginas del trabajo (A�adido y en PascalCase)
    Tema VARCHAR(500) NOT NULL,                -- Tema del trabajo (A�adido y en PascalCase)
    CONSTRAINT FK_Trabajos_Evaluaciones FOREIGN KEY (EvaluacionID)
        REFERENCES Evaluaciones(EvaluacionID)
        ON DELETE CASCADE,
    CONSTRAINT CK_NumPaginas CHECK (NumPaginas > 0)
);

-- 4. Tabla para Presentaciones
-- Almacena atributos espec�ficos de las presentaciones, con una clave for�nea a Evaluaciones
CREATE TABLE Presentaciones (
    PresentacionID INT PRIMARY KEY IDENTITY(1,1),
    EvaluacionID INT UNIQUE NOT NULL,          -- Clave for�nea, debe ser �nica para cada evaluaci�n
    Duracion INT NOT NULL,                     -- Duraci�n de la presentaci�n en minutos (A�adido y en PascalCase)
    TamanoAudiencia INT NOT NULL,              -- Tama�o de la audiencia (A�adido y en PascalCase)
    CONSTRAINT FK_Presentaciones_Evaluaciones FOREIGN KEY (EvaluacionID)
        REFERENCES Evaluaciones(EvaluacionID)
        ON DELETE CASCADE,
    CONSTRAINT CK_DuracionPresentacion CHECK (Duracion > 0),
    CONSTRAINT CK_TamanoAudiencia CHECK (TamanoAudiencia > 0)
);
GO