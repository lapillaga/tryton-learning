from trytond.model import ModelSQL, ModelView, fields


class Invoice(ModelSQL, ModelView):
    """
    Invoice Model
    """
    __name__ = 'learning.invoice'

    company = fields.Many2One(
        'company.company',
        'Company',
    )
    date = fields.Date(
        'Date',
        required=True,
    )
    number = fields.Char('Number', size=5)
    has_number = fields.Function(
        fields.Boolean('Has Number'),
        getter='get_has_number',
        searcher='search_has_number',
    )

    @classmethod
    def search_has_number(cls, name, clause):
        return [('number', '!=', None)]

    def get_has_number(self, name):
        return bool(self.number)
