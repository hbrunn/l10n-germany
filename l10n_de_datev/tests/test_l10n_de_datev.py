# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import base64
import datetime
import zipfile
from odoo.tests.common import TransactionCase


class TestL10nDeDatevExport(TransactionCase):
    def setUp(self):
        super().setUp()
        self.range = self.env["date.range"].create(
            {
                "name": "testrange",
                "type_id": self.env.ref("account_fiscal_year.fiscalyear").id,
                "date_start": datetime.date.today(),
                "date_end": datetime.date.today(),
            }
        )
        self.wizard = self.env["l10n_de_datev.export"].create(
            {
                "fiscalyear_id": self.range.id,
                "period_ids": [(6, 0, self.range.ids)],
            }
        )

    def test_happy_flow(self):
        self.wizard.action_generate()
        zip_file = base64.b64decode(self.wizard.file_data)
        # TODO actually test something
