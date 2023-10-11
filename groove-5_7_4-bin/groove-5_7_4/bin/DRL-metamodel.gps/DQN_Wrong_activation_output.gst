<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<gxl xmlns="http://www.gupro.de/GXL/gxl-1.0.dtd">
	<graph role="graph" edgeids="false" edgemode="directed" id="RL">
		<node id="n0">
			<attr name="layout">
				<string>108 93 83 18</string>
			</attr>
		</node>
		<node id="n1">
			<attr name="layout">
				<string>443 77 147 72</string>
			</attr>
		</node>
		<node id="n2">
			<attr name="layout">
				<string>429 243 122 54</string>
			</attr>
		</node>
		<node id="n3">
			<attr name="layout">
				<string>260 258 133 54</string>
			</attr>
		</node>
		<node id="n4">
			<attr name="layout">
				<string>581 288 141 54</string>
			</attr>
		</node>
		<node id="n5">
			<attr name="layout">
				<string>837 94 65 18</string>
			</attr>
		</node>
		<node id="n6">
			<attr name="layout">
				<string>128 518 126 36</string>
			</attr>
		</node>
		<node id="n7">
			<attr name="layout">
				<string>523 525 53 18</string>
			</attr>
		</node>
		<node id="n8">
			<attr name="layout">
				<string>809 512 95 36</string>
			</attr>
		</node>
		<node id="n9">
			<attr name="layout">
				<string>789 604 116 72</string>
			</attr>
		</node>
		<edge from="n0" to="n0">
			<attr name="label">
				<string>type:DRL-Program</string>
			</attr>
		</edge>
		<edge from="n0" to="n1">
			<attr name="label">
				<string>uses</string>
			</attr>
		</edge>
		<edge from="n0" to="n6">
			<attr name="label">
				<string>interacts-with</string>
			</attr>
		</edge>
		<edge from="n1" to="n1">
			<attr name="label">
				<string>type:DQN</string>
			</attr>
		</edge>
		<edge from="n1" to="n2">
			<attr name="label">
				<string>has</string>
			</attr>
		</edge>
		<edge from="n1" to="n3">
			<attr name="label">
				<string>has</string>
			</attr>
		</edge>
		<edge from="n1" to="n4">
			<attr name="label">
				<string>has</string>
			</attr>
		</edge>
		<edge from="n1" to="n5">
			<attr name="label">
				<string>has</string>
			</attr>
		</edge>
		<edge from="n1" to="n1">
			<attr name="label">
				<string>let:gamma = real:0.99</string>
			</attr>
		</edge>
		<edge from="n1" to="n1">
			<attr name="label">
				<string>let:alpha = real:0.01</string>
			</attr>
		</edge>
		<edge from="n1" to="n1">
			<attr name="label">
				<string>let:is_update_eq_valid = bool:true</string>
			</attr>
		</edge>
		<edge from="n1" to="n1">
			<attr name="label">
				<string>let:action_indication = bool:true</string>
			</attr>
		</edge>
		<edge from="n2" to="n2">
			<attr name="label">
				<string>type:Hyperparameters</string>
			</attr>
		</edge>
		<edge from="n2" to="n2">
			<attr name="label">
				<string>let:batchSize = int:32</string>
			</attr>
		</edge>
		<edge from="n2" to="n2">
			<attr name="label">
				<string>let:epochCount = int:50000</string>
			</attr>
		</edge>
		<edge from="n3" to="n3">
			<attr name="label">
				<string>type:Exploration</string>
			</attr>
		</edge>
		<edge from="n3" to="n3">
			<attr name="label">
				<string>let:decay_factor = real:0.9999</string>
			</attr>
		</edge>
		<edge from="n3" to="n3">
			<attr name="label">
				<string>let:explorationRate = real:0.99</string>
			</attr>
		</edge>
		<edge from="n3" to="n3">
			<attr name="label">
				<string>let:update_exploration_rate = bool:true</string>
			</attr>
		</edge>
		<edge from="n4" to="n4">
			<attr name="label">
				<string>type:target-network</string>
			</attr>
		</edge>
		<edge from="n4" to="n5">
			<attr name="label">
				<string>Q-values_to_train</string>
			</attr>
		</edge>
		<edge from="n4" to="n4">
			<attr name="label">
				<string>let:updateFrequency = int:25</string>
			</attr>
		</edge>
		<edge from="n5" to="n5">
			<attr name="label">
				<string>type:Q-network</string>
			</attr>
		</edge>
		<edge from="n5" to="n4">
			<attr name="label">
				<string>periodically_updates</string>
			</attr>
		</edge>
		<edge from="n5" to="n8">
			<attr name="label">
				<string>send_action</string>
			</attr>
		</edge>
		<edge from="n5" to="n5">
			<attr name="label">
				<string>let:last_layer_activation = "relu"</string>
			</attr>
		</edge>
		<edge from="n6" to="n6">
			<attr name="label">
				<string>type:Environment</string>
			</attr>
		</edge>
		<edge from="n6" to="n7">
			<attr name="label">
				<string>starts-by</string>
			</attr>
		</edge>
		<edge from="n6" to="n6">
			<attr name="label">
				<string>let:name = "CartPole-v0"</string>
			</attr>
		</edge>
		<edge from="n7" to="n7">
			<attr name="label">
				<string>type:Initialize</string>
			</attr>
		</edge>
		<edge from="n7" to="n8">
			<attr name="label">
				<string>continues-by</string>
			</attr>
		</edge>
		<edge from="n8" to="n8">
			<attr name="label">
				<string>type:Step</string>
			</attr>
		</edge>
		<edge from="n8" to="n8">
			<attr name="label">
				<string>repeats</string>
			</attr>
			<attr name="layout">
				<string>500 -9 927 479 1025 478 927 479 11</string>
			</attr>
		</edge>
		<edge from="n8" to="n5">
			<attr name="label">
				<string>receive_state</string>
			</attr>
		</edge>
		<edge from="n8" to="n9">
			<attr name="label">
				<string>detect</string>
			</attr>
		</edge>
		<edge from="n9" to="n9">
			<attr name="label">
				<string>type:Terminalstate</string>
			</attr>
		</edge>
		<edge from="n9" to="n8">
			<attr name="label">
				<string>reset</string>
			</attr>
		</edge>
		<edge from="n9" to="n7">
			<attr name="label">
				<string>close</string>
			</attr>
		</edge>
	</graph>
</gxl>