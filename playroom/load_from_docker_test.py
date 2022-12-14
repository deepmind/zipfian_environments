# Copyright 2022 DeepMind Technologies Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Tests for dm_zipf_playroom.zipfs_playroom.load_from_docker."""

from absl import flags
from absl.testing import absltest
from absl.testing import parameterized
from dm_env import test_utils

from zipfian_environments import playroom as zipfs_playroom

DOCKER_IMAGE_NAME = flags.DEFINE_string(
    'docker_image_name', None,
    'Name of the Docker image that contains the Zipfian Distributions Tasks. '
    'If None, uses the default dm_zipf_playroom name')


class LoadFromDockerTest(test_utils.EnvironmentTestMixin, absltest.TestCase):

  def make_object_under_test(self):
    return zipfs_playroom.load_from_docker(
        name=DOCKER_IMAGE_NAME.value,
        settings=zipfs_playroom.EnvironmentSettings(
            seed=123, level_name='lift/lift_shape_zipf2'))


class ZipfianDistributionsTaskTest(parameterized.TestCase):

  @parameterized.parameters(
      zipfs_playroom.ZIPFIAN_DISTRIBUTIONS_TASK_LEVEL_NAMES)
  def test_load_level(self, level_name):
    self.assertIsNotNone(
        zipfs_playroom.load_from_docker(
            name=DOCKER_IMAGE_NAME.value,
            settings=zipfs_playroom.EnvironmentSettings(
                seed=123, level_name=level_name)))


if __name__ == '__main__':
  absltest.main()
