from urllib.parse import unquote

from flask import redirect
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Tag

from logger import logger
from model import Session, Student
from model.model import Model
from model.pipeline import Pipeline
from model.preprocessor import PreProcessor
from schemas import StudentViewSchema, ErrorSchema, show_students, StudentSchema, show_single_student, \
    StudentSearchSchema

# Instanciando o objeto OpenAPI
app = OpenAPI(__name__)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
student_tag = Tag(name="Estudante", description="Adição, visualização, remoção e predição de alunos")


@app.get('/', tags=[home_tag])
def home():
    """
    Redireciona para openapi
    """
    return redirect('/openapi')


@app.get('/students', tags=[student_tag], responses={"200": StudentViewSchema, "404": ErrorSchema})
def get_students():
    """"Lista com todos os estudantes
    Args: none
    Returns: todos os pacientes.
    """
    logger.debug("Pegando dados sobre todos estudantes.")

    session = Session()
    students = session.query(Student).all()

    if not students:
        # Se não houver estudantes
        return {"Estudantes": []}, 200
    else:
        logger.debug(f"%d estudantes encontrados" % len(students))
        print(students)
        return show_students(students), 200


@app.post('/add_student', tags=[student_tag],
          responses={"200": StudentViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def add_student(form: StudentSchema):
    """"Adiciona um novo estudante a base de dados"""

    # Recuperando os dados do formuário
    name = form.name
    gender = form.gender
    attendance_rate = form.attendance_rate
    study_hours_per_week = form.study_hours_per_week
    previous_grade = form.previous_grade
    extracurricular_activities = form.extracurricular_activities
    parental_support = form.parental_support

    # Preparando os dados para o modelo
    X_input = PreProcessor.prepare_form(form)

    # Carregando o modelo
    model_path = './MachineLearning/pipelines/rf_student_pipeline.pkl'
    modelo = Pipeline.load_pipeline(model_path)

    # Realizando precição
    final_grade = int(Model.preditor(modelo, X_input)[0])

    student_obj = Student(
        name=name,
        gender=gender,
        attendance_rate=attendance_rate,
        study_hours_per_week=study_hours_per_week,
        previous_grade=previous_grade,
        extracurricular_activities=extracurricular_activities,
        parental_support=parental_support,
        final_grade=final_grade
    )
    logger.debug(f"Adicionando produto de nome: '{student_obj.name}'")

    try:
        session = Session()

        # Checando se paciente já existe na base
        if session.query(Student).filter(Student.name == form.name).first():
            error_msg = "Estudante já existente na base :"
            logger.warning(f"Erro ao adicionar estudante '{student_obj.name}', {error_msg}")
            return {"message": error_msg}, 409

        session.add(student_obj)
        session.commit()
        logger.debug(f"Adicionado estudante de nome: '{student_obj.name}'")
        return show_single_student(student_obj), 200

    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar estudante '{student_obj.name}', {error_msg}, {e}")
        return {"message": error_msg}, 400


@app.delete('/delete_student', tags=[student_tag], responses={"200": StudentViewSchema, "404": ErrorSchema})
def delete_student(query: StudentSearchSchema):
    student_name = unquote(query.name)
    logger.debug(f"Deletando dados sobre estudante #{student_name}")

    session = Session()

    student = session.query(Student).filter(Student.name == student_name).first()

    if not student:
        error_msg = "Estudante não encontrado na base :/"
        logger.warning(f"Erro ao deletar estudante '{student_name}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(student)
        session.commit()
        logger.debug(f"Deletado estudante #{student_name}")
        return {"message": f"Estudante {student_name} removido com sucesso!"}, 200


if __name__ == '__main__':
    app.run(debug=True)
