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
    horarios = range(6,13,2)
    horarios.append(24)
    form=SQLFORM.factory(db.paciente_medicamento,Field('frequencia',label='Frequência(em horas)',requires=IS_IN_SET(horarios, zero=T('Escolha um'))),submit_button='Salvar',formstyle='divs')
    
    if form.process().accepted:
        frequencia = int(form.vars.frequencia)
        del form.vars.frequencia
        if frequencia == 10:
            iteracoes = 12
        else:
            iteracoes = 24/frequencia 
            
        for _ in xrange(iteracoes):
           horario = form.vars.horario
           form.vars.update(horario=horario.replace(hour=horario.hour+frequencia if horario.hour+frequencia < 24 else (horario.hour+frequencia) -24))
           db.paciente_medicamento.insert(**form.vars)
                
        
            
            
            
        
        
        response.flash = 'Salvo com sucesso!'
    elif form.errors:
        print form.vars
        response.flash = 'Formulários contém erros!'
    return dict(form=form)
