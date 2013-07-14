# coding: utf8
# try something like
def paciente(): 
    form=SQLFORM(db.pacientes,submit_button='Salvar',formstyle='divs')
    if form.process().accepted:
        response.flash = 'Salvo com sucesso!'
    elif form.errors:
        response.flash = 'Formulários contém erros!'
    return dict(form=form)
    
def medicamento(): 
    form=SQLFORM(db.medicamentos,submit_button='Salvar',formstyle='divs')
    if form.process().accepted:
        response.flash = 'Salvo com sucesso!'
    elif form.errors:
        response.flash = 'Formulários contém erros!'
    return dict(form=form)


    
def estoque(): 
    form=SQLFORM(db.estoque,submit_button='Salvar',formstyle='divs')
    if form.process().accepted:
        response.flash = 'Salvo com sucesso!'
    elif form.errors:
        response.flash = 'Formulários contém erros!'
    return dict(form=form)
    
def horarios(): 
    form=SQLFORM(db.paciente_medicamento,submit_button='Salvar',formstyle='divs')
    if form.process().accepted:
        
        response.flash = 'Salvo com sucesso!'
    elif form.errors:
    
        response.flash = 'Formulários contém erros!'
    return dict(form=form)
